# Generated by Django 3.0.5 on 2021-09-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder', '0006_auto_20210905_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='price',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
