# Generated by Django 3.2.8 on 2021-10-24 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RSRujukan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=40)),
                ('umur', models.IntegerField()),
                ('noTelfon', models.CharField(max_length=13)),
                ('rumahSakit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSRujukan.rumahsakit')),
            ],
        ),
    ]
