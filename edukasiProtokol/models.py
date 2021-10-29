from typing import Tuple
from django.db import models
from django.db.models.fields import DateField

class Artikel(models.Model):
    judul = models.CharField(max_length=80)
    image_link = models.CharField(max_length=400, default = '')
    artikel_link = models.CharField(max_length=400, default= '')
    tanggal_publish = models.DateField(auto_now=True)
    publisher = models.CharField(max_length=30)
    deskripsi = models.TextField()