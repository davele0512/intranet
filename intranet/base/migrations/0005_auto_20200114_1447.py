# Generated by Django 2.2.4 on 2020-01-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_people_division'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='job_title',
            field=models.CharField(help_text="Select the person's job title", max_length=254, verbose_name='Job title'),
        ),
    ]
