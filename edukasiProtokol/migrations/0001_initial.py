# Generated by Django 3.2.8 on 2021-10-25 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('tanggal_publish', models.DateField()),
                ('penulis', models.CharField(max_length=30)),
                ('isi', models.TextField()),
            ],
        ),
    ]