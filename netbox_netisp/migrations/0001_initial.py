# Generated by Django 3.1.3 on 2021-02-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, null=True)),
                ("last_updated", models.DateTimeField(auto_now=True, null=True)),
                ("first_name", models.CharField(max_length=30)),
                ("middle_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
