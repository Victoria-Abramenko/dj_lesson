# Generated by Django 5.2.1 on 2025-06-13 19:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0006_alter_lessonfordb_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=50)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lessonfordb',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='lesson_1.category'),
        ),
        migrations.AddField(
            model_name='lessonfordb',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='lesson_1.tagposts'),
        ),
    ]
