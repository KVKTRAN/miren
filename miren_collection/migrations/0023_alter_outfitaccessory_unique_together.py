# Generated by Django 4.0 on 2022-01-26 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0022_alter_outfitaccessory_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='outfitaccessory',
            unique_together={('outfit', 'accessory')},
        ),
    ]