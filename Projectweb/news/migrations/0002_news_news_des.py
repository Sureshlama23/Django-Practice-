# Generated by Django 5.0 on 2024-01-06 11:03

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_des',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
