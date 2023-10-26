# Generated by Django 4.2.6 on 2023-10-24 02:33

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
            name="RequestBuku",
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
                ("judul_buku", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
                ("tahun_publikasi", models.IntegerField()),
                ("tanggal_request", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StatusRequest",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Diterima", "Diterima"),
                            ("Ditolak", "Ditolak"),
                        ],
                        default="Pending",
                        max_length=20,
                    ),
                ),
                (
                    "buku",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="request_buku.requestbuku",
                    ),
                ),
            ],
        ),
    ]