from django.db import models
from django.db.models.fields import DateField

class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    image_link = models.CharField(max_length=400, default = '')
    artikel_link = models.CharField(max_length=400, default= '')
    tanggal_publish = models.DateField()
    publisher = models.CharField(max_length=30)
    deskripsi = models.CharField(max_length=200, default='')