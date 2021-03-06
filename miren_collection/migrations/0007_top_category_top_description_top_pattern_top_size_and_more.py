# Generated by Django 4.0 on 2022-01-19 19:16

from django.db import migrations, models
import miren_collection.models


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0006_alter_top_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='top',
            name='category',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='top',
            name='description',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='top',
            name='pattern',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='top',
            name='size',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='top',
            name='image',
            field=models.ImageField(upload_to=miren_collection.models.top_rename),
        ),
        migrations.AlterField(
            model_name='top',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
