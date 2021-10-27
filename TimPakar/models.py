from django.db import models

# Create your models here.
class Regist(models.Model):
    nama = models.CharField(max_length=30)
    tempatBertugas = models.CharField(max_length=30)
    asalUniversitas = models.CharField(max_length=30)
    pesan = models.TextField()
