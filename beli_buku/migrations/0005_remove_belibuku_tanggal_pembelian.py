# Generated by Django 4.2.6 on 2023-10-29 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beli_buku', '0004_belibuku_tanggal_pembelian'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='belibuku',
            name='tanggal_pembelian',
        ),
    ]
