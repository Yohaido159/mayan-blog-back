# Generated by Django 3.0.5 on 2020-05-04 07:55

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200503_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='desc',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
