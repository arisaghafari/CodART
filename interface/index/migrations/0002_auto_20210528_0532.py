# Generated by Django 3.2.3 on 2021-05-28 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refactoring',
            name='has_description',
        ),
        migrations.RemoveField(
            model_name='refactoring',
            name='has_example',
        ),
        migrations.AddField(
            model_name='refactoring',
            name='post_conditions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='refactoring',
            name='pre_conditions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
