# Generated by Django 3.0.5 on 2021-09-05 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0005_projects_htmlpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='description',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='youtubelink',
        ),
    ]
