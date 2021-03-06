# Generated by Django 4.0 on 2022-01-22 18:08

from django.db import migrations, models
import miren_collection.models


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0016_delete_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='top',
            name='description',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='top',
            name='image',
            field=models.ImageField(default=1, upload_to=miren_collection.models.top_rename),
            preserve_default=False,
        ),
    ]
