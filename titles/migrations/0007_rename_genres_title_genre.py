# Generated by Django 4.2.6 on 2023-10-10 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0006_alter_category_slug_alter_genre_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='title',
            old_name='genres',
            new_name='genre',
        ),
    ]
