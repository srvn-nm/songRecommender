# Generated by Django 5.0.3 on 2024-03-13 20:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Request",
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
                ("email", models.EmailField(max_length=254)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "Pending"),
                            ("failure", "Failure"),
                            ("ready", "Ready"),
                            ("done", "Done"),
                        ],
                        default="pending",
                        max_length=20,
                    ),
                ),
                ("song_id", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
