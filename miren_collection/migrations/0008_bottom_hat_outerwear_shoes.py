# Generated by Django 4.0 on 2022-01-19 19:36

from django.db import migrations, models
import miren_collection.models


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0007_top_category_top_description_top_pattern_top_size_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('pattern', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=miren_collection.models.top_rename)),
            ],
        ),
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('pattern', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=miren_collection.models.top_rename)),
            ],
        ),
        migrations.CreateModel(
            name='Outerwear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('pattern', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=miren_collection.models.top_rename)),
            ],
        ),
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('pattern', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('size', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to=miren_collection.models.top_rename)),
            ],
        ),
    ]
