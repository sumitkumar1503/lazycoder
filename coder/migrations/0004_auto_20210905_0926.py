# Generated by Django 3.0.5 on 2021-09-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0003_projects_longnameurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.CharField(max_length=60000),
        ),
    ]