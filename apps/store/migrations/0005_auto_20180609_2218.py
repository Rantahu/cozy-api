# Generated by Django 2.0.1 on 2018-06-09 22:18

import apps.store.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(upload_to=apps.store.models.scramble_uploaded_filename),
        ),
    ]
