# Generated by Django 4.1 on 2022-09-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="MyWatchList",
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
                ("watched", models.BooleanField()),
                ("title", models.CharField(max_length=50)),
                ("rating", models.CharField(max_length=1)),
                ("release_date", models.CharField(max_length=4)),
                ("review", models.TextField()),
            ],
        ),
    ]
