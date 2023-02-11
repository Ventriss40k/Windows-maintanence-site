# Generated by Django 4.1.4 on 2023-01-30 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0006_archive_name_alter_archive_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutCompany",
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
                ("photo", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="AboutOwner",
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
                ("photo", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="AboutStaff",
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
                ("photo", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name="About",
        ),
    ]