# Generated by Django 4.2.6 on 2023-10-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pinjam_buku', '0002_remove_pinjambuku_metode_pembayaran'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinjambuku',
            name='alamat',
            field=models.TextField(blank=True, default='UI', null=True),
        ),
        migrations.AlterField(
            model_name='pinjambuku',
            name='durasi',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='pinjambuku',
            name='nomor_telepon',
            field=models.IntegerField(blank=True, default=62, null=True),
        ),
    ]
