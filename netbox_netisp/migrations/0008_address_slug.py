# Generated by Django 3.1.3 on 2021-02-15 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_netisp", "0007_auto_20210215_2105"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="slug",
            field=models.SlugField(null=True, unique=True),
        ),
    ]
