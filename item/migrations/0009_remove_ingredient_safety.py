# Generated by Django 5.0.4 on 2024-05-25 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_rename_ingredient_item_ingredients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='safety',
        ),
    ]