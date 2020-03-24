# Generated by Django 2.2.7 on 2020-03-20 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('lesson', '0010_delete_lessonunit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='custom_title',
        ),
        migrations.AddField(
            model_name='level',
            name='thumb_description',
            field=models.TextField(blank=True, help_text='description of the lesson'),
        ),
        migrations.AddField(
            model_name='level',
            name='thumb_image',
            field=models.ForeignKey(help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
