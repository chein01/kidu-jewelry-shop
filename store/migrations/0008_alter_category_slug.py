# Generated by Django 5.0.7 on 2024-08-03 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(editable=False, max_length=55, unique=True, verbose_name='Slug'),
        ),
    ]
