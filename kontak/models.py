from django.db import models

# Create your models here.


class Kontak(models.Model):
    nama = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    nomor_kontak = models.CharField(max_length=100)
