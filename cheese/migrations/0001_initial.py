# Generated by Django 4.2.5 on 2023-09-18 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cheese",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("origin_country", models.CharField(max_length=200)),
                ("type", models.CharField(max_length=200)),
            ],
        ),
    ]
