# Generated by Django 3.1.3 on 2021-02-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_netisp", "0002_customer_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("street_number", models.IntegerField()),
                ("street_ordinance", models.CharField(max_length=1)),
                ("street_name", models.CharField(max_length=255)),
                ("street_suffix", models.CharField(max_length=255)),
                ("city", models.CharField(max_length=255)),
                ("state_code", models.CharField(max_length=2)),
                ("zip", models.CharField(max_length=10)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
