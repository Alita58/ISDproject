# Generated by Django 3.0.3 on 2020-04-30 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_auto_20200430_0545'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=10.3, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1),
        ),
    ]
