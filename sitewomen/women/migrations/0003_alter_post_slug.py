# Generated by Django 4.0.6 on 2024-01-07 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0002_alter_post_options_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=255, unique=True),
        ),
    ]
