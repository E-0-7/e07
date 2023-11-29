# Generated by Django 4.2.7 on 2023-11-29 08:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BukuDonasi",
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
                ("donator", models.CharField(max_length=255)),
                ("donation_date", models.DateField(default=datetime.date.today)),
                ("donation_amount", models.IntegerField()),
                ("title", models.CharField(max_length=255)),
                ("author", models.CharField(max_length=255)),
                ("year", models.IntegerField()),
                ("image_url", models.URLField(null=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("DITERIMA", "DITERIMA"),
                            ("DITOLAK", "DITOLAK"),
                        ],
                        default="PENDING",
                        max_length=15,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
