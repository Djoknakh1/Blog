# Generated by Django 4.0.6 on 2024-01-19 12:29

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_tags_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='level',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='lft',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='women.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='rght',
            field=models.PositiveIntegerField(default=1, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False),
            preserve_default=False,
        ),
    ]
