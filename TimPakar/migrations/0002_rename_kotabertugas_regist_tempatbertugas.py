# Generated by Django 3.2.8 on 2021-10-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TimPakar', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='regist',
            old_name='kotaBertugas',
            new_name='tempatBertugas',
        ),
    ]