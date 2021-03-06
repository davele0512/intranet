# Generated by Django 2.2.7 on 2020-03-19 05:24

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('lesson', '0002_auto_20200319_1200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lessondetail',
            old_name='lesson_image',
            new_name='banner_image',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='lesson_break',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='lesson_close',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='lesson_section_1',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='lesson_section_2',
        ),
        migrations.RemoveField(
            model_name='lessondetail',
            name='lesson_warmup',
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='breaktime',
            field=wagtail.core.fields.StreamField([('name', wagtail.core.blocks.CharBlock()), ('description', wagtail.core.blocks.CharBlock()), ('link_text', wagtail.core.blocks.CharBlock()), ('link_cta', wagtail.core.blocks.CharBlock())], blank=True, help_text='Breaktime activity'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='section_1',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('headting_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))], blank=True, verbose_name='Block 1'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='section_2',
            field=wagtail.core.fields.StreamField([('heading_block', wagtail.core.blocks.StructBlock([('headting_text', wagtail.core.blocks.CharBlock(classname='title', required=True)), ('size', wagtail.core.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a header size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', template='blocks/paragraph_block.html')), ('image_block', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.core.blocks.CharBlock(required=False)), ('attribution', wagtail.core.blocks.CharBlock(required=False))])), ('block_quote', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.TextBlock()), ('attribute_name', wagtail.core.blocks.CharBlock(blank=True, label='e.g. Mary Berry', required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert an embed URL e.g https://www.youtube.com/embed/SGJFWirQ3ks', icon='fa-s15', template='blocks/embed_block.html'))], blank=True, verbose_name='Block 2'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='warmup',
            field=models.ForeignKey(blank=True, help_text='Choose an activity to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Warm Up'),
        ),
        migrations.AddField(
            model_name='lessondetail',
            name='wrapup',
            field=models.ForeignKey(blank=True, help_text='Choose an activity to link to for the Call to Action', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page', verbose_name='Wrap Up'),
        ),
        migrations.AlterField(
            model_name='lessondetail',
            name='custom_title',
            field=models.CharField(blank=True, help_text='Overwrite the default title if needed', max_length=100, null=True),
        ),
    ]
