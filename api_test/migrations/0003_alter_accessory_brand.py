# Generated by Django 4.0 on 2022-01-22 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0002_brand_accessory_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accessories', to='api_test.brand'),
        ),
    ]
