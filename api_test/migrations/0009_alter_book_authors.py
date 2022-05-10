# Generated by Django 4.0 on 2022-01-28 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_test', '0008_author_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='books', to='api_test.Author'),
        ),
    ]