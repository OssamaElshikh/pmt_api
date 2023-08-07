# Generated by Django 4.2.4 on 2023-08-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("name", models.CharField(max_length=50)),
                ("phone", models.IntegerField(max_length=15)),
                ("speed", models.CharField(max_length=20)),
                ("pop_name", models.CharField(max_length=50)),
                ("dslam_hostname", models.CharField(max_length=50)),
                ("frame", models.IntegerField(max_length=50)),
                ("attainable_speed", models.IntegerField(max_length=50)),
            ],
        ),
    ]
