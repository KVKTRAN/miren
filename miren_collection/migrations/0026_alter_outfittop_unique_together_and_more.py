# Generated by Django 4.0 on 2022-01-27 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0025_outfit_bottom_outfit_outerwear_outfit_shoe_outfittop'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='outfittop',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='outfittop',
            name='outfit',
        ),
        migrations.RemoveField(
            model_name='outfittop',
            name='top',
        ),
        migrations.AddField(
            model_name='outfit',
            name='accessory',
            field=models.ManyToManyField(blank=True, related_name='accessories', to='miren_collection.Accessory'),
        ),
        migrations.AddField(
            model_name='outfit',
            name='top',
            field=models.ManyToManyField(blank=True, related_name='tops', to='miren_collection.Top'),
        ),
        migrations.DeleteModel(
            name='OutfitAccessory',
        ),
        migrations.DeleteModel(
            name='OutfitTop',
        ),
    ]