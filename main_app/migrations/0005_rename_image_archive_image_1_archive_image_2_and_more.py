# Generated by Django 4.1.4 on 2023-01-30 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0004_archive_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="archive",
            old_name="image",
            new_name="image_1",
        ),
        migrations.AddField(
            model_name="archive",
            name="image_2",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AddField(
            model_name="archive",
            name="image_3",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]