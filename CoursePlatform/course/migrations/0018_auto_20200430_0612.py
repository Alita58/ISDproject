# Generated by Django 3.0.3 on 2020-04-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_auto_20200430_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prerequisite',
            field=models.TextField(blank=True, help_text='What Student Should Before Enrolling to this Course', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='who_this_course_is_for',
            field=models.TextField(blank=True, help_text='Who this course can target', null=True),
        ),
    ]