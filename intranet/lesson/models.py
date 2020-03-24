from __future__ import unicode_literals

from django import forms
from django.db import models
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    PageChooserPanel,
    StreamFieldPanel,
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.search import index
from wagtail.snippets.models import register_snippet

from taggit.models import TaggedItemBase


from ..base.blocks import BaseStreamBlock, CardBlock


@register_snippet
class LessonCategory(models.Model):
    """Blog catgory for a snippet."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify lessons by this category',
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    class Meta:
        verbose_name = "Lesson Category"
        verbose_name_plural = "Lesson Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


@register_snippet
class InclassActivitySnippet(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify lessons by this activity',
    )
    class Meta:
        verbose_name = "Inclass Activitiy"
        verbose_name_plural = "Inclass Activities"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Level(RoutablePageMixin, Page):

    templates = "lesson/lesson_list.html"

    thumb_description = models.TextField(
        help_text='description of the lesson',
        blank=True
    )

    thumb_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Landscape mode only; horizontal width between 1000px and 3000px.'
    )

    content_panels = Page.content_panels + [
        FieldPanel('thumb_description', classname="full"),
        ImageChooserPanel('thumb_image'),
    ]

    @property
    def get_child_pages(self):
        return self.get_children().public().live()
        # return self.get_children().public().live().values("id", "title", "slug")


    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["lessons"] = LessonDetail.objects.live().public()
        context["categories"] = LessonCategory.objects.all()
        all_lessons = LessonDetail.objects.live().public().order_by('-first_published_at')
        
        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_lessons = all_lessons.filter(tags__slug__in=[tags])
        
        # Paginate all posts by 2 per page
        paginator = Paginator(all_lessons, 2)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            lessons  = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            lessons  = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            lessons  = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        
        context["lessons"] = lessons
        return context


    @route(r"^july-2019/$", name="july_2019")
    @route(r"^year/(\d+)/(\d+)/$", name="lesson_created_by_year")
    def lessons_by_year(self, request, year=None, month=None):
        context = self.get_context(request)
        # Implement your BlogDetailPage filter. Maybe something like this:
        # if year is not None and month is not None:
        #     posts = BlogDetailPage.objects.live().public().filter(year=year, month=month)
        # else:
        #     # No year and no month were set, assume this is july-2019 only posts
        #     posts = BlogDetailPage.objects.live().public().filter(year=2019, month=07)
        # print(year)
        # print(month)
        # context["posts"] = posts

        # Note: The below template (latest_posts.html) will need to be adjusted
        return render(request, "lesson/latest_lessons.html", context)

    @route(r"^category/(?P<cat_slug>[-\w]*)/$", name="category_view")
    def category_view(self, request, cat_slug):
        """Find lessons based on a category."""
        context = self.get_context(request)

        try:
            # Look for the blog category by its slug.
            category = LessonCategory.objects.get(slug=cat_slug)
        except Exception:
            # Blog category doesnt exist (ie /blog/category/missing-category/)
            # Redirect to self.url, return a 404.. that's up to you!
            category = None

        if category is None:
            # This is an additional check.
            # If the category is None, do something. Maybe default to a particular category.
            # Or redirect the user to /blog/ ¯\_(ツ)_/¯
            pass

        context["lessons"] = LessonDetail.objects.live().public().filter(categories__in=[category])

        # Note: The below template (latest_posts.html) will need to be adjusted
        return render(request, "lesson/latest_lessons.html", context)


    @route(r'^latest/$', name="latest_lessons")
    def latest_lessons_only_shows_last_5(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        context["lessons"] = context["lessons"][:2]
        return render(request, "lesson/latest_lessons.html", context)

    subpage_types = ['LessonDetail']


class LessonTag(TaggedItemBase):
    content_object = ParentalKey(
        'LessonDetail',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class LessonDetail(RoutablePageMixin, Page):

    template = "lesson/lesson_detail.html"

    subpage_types = []
    parent_page_types = ['lesson.Level']
    tags = ClusterTaggableManager(through=LessonTag, blank=True)

    categories = ParentalManyToManyField("lesson.LessonCategory", blank=True)

    lesson_description = models.TextField(
        help_text='description of the lesson',
        blank=True
    )

    lesson_objective = models.TextField(
        help_text='objectives of the lesson',
        blank=False
    )

    warmup = RichTextField(
        verbose_name="Warm Up",
        null=True,
        blank=True
    )
 
    section_1 = StreamField(
        BaseStreamBlock(),
        verbose_name="Block 1", 
        null=True,
        blank=True
    )

    breaktime = RichTextField(
        verbose_name="Breaktime",
        null=True,
        blank=True
    )
 
    section_2 = StreamField(
        BaseStreamBlock(),
        null=True,
        verbose_name="Block 2", 
        blank=True
    )

    wrapup = RichTextField(
        verbose_name="Wrap Up",
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('lesson_description'),
            FieldPanel('lesson_objective'),
            FieldPanel("tags"),
    
        ], heading="Lesson Introduction", classname="collapsible"),
        MultiFieldPanel(
            [
                FieldPanel("categories", widget=forms.CheckboxSelectMultiple)
            ],
            heading="Categories"
        ),
        MultiFieldPanel([
            FieldPanel('warmup'),
        ], heading="Lesson Opening"),
        MultiFieldPanel([
            StreamFieldPanel('section_1'),
            FieldPanel('breaktime'),
            StreamFieldPanel('section_2'),
        ], heading="Lesson Main Content",),
        MultiFieldPanel([
            FieldPanel('wrapup'),
        ], heading="Lesson Summary ",),
    ]

    subpage_types = []


    # @route(r'^subscribe/$')
    # def the_subscribe_page(self, request, *args, **kwargs):
    #     context = self.get_context(request, *args, **kwargs)
    #     context['test'] = "Hello World 123"
    #     return render(request, "lesson/subscribe.html", context)
    #     pass





