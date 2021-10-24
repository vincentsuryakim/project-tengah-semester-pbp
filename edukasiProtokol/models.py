from django.db import models
from django.db.models.fields import DateField

class Artikel(models.Model):
    Judul = models.CharField(max_length=300)
    Tanggal_publish = models.DateField
    Penulis = models.CharField(max_length=300)
    Isi = models.TextField()