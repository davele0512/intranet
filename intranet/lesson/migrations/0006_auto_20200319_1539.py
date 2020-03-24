# Generated by Django 2.2.7 on 2020-03-19 08:39

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.contrib.routable_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('lesson', '0005_auto_20200319_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='LessonCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, help_text='A slug to identify lessons by this category', max_length=255, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Lesson Category',
                'verbose_name_plural': 'Lesson Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LessonTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='lesson.LessonDetail')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesson_lessontag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('custom_title', models.CharField(help_text='Overwrite the default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.routable_page.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.DeleteModel(
            name='LessonList',
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='lesson.LessonCategory'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='lesson.LessonTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
