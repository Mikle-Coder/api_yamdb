# Generated by Django 4.2.6 on 2023-10-10 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_title_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=models.CharField(max_length=255),
        ),
    ]