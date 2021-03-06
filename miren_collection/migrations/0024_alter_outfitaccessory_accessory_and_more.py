# Generated by Django 4.0 on 2022-01-26 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miren_collection', '0023_alter_outfitaccessory_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outfitaccessory',
            name='accessory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outfits', to='miren_collection.accessory'),
        ),
        migrations.AlterField(
            model_name='outfitaccessory',
            name='outfit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='miren_collection.outfit'),
        ),
    ]
