# Generated by Django 3.1.3 on 2021-02-15 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_netisp", "0006_auto_20210215_2054"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customer",
            old_name="birthday",
            new_name="birthdate",
        ),
    ]
