# Generated by Django 3.2.8 on 2021-10-27 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edukasiProtokol', '0008_alter_artikel_tanggal_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='tanggal_publish',
            field=models.DateField(auto_now_add=True),
        ),
    ]
