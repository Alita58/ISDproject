# Generated by Django 3.0.3 on 2020-04-30 07:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0023_auto_20200430_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecontent',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(help_text='Enter the Video url of youtube or vimeo'),
        ),
    ]