# Generated by Django 5.2.1 on 2025-06-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0002_alter_lessonfordb_options_lessonfordb_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonfordb',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
