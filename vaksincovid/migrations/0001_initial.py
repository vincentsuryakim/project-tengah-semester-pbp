# Generated by Django 3.2.8 on 2021-10-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dataVaksin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=512)),
                ('deskripsi', models.TextField()),
                ('presentasi', models.TextField()),
                ('usia', models.CharField(max_length=512)),
                ('jadwal', models.TextField()),
                ('dosis1', models.TextField()),
                ('dosis2', models.TextField()),
            ],
        ),
    ]
