# Generated by Django 4.0 on 2022-01-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='top',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
