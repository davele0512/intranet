# Generated by Django 2.2.7 on 2020-03-19 05:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailimages', '0001_squashed_0021'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LessonDetailPage',
            new_name='LessonDetail',
        ),
        migrations.RenameModel(
            old_name='LessonListingPage',
            new_name='LessonList',
        ),
    ]
