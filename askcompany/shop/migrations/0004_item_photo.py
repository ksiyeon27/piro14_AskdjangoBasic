# Generated by Django 2.2.17 on 2021-01-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210116_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
