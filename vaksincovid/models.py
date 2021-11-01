from django.db import models

# Create your models here.
class dataVaksin(models.Model):
    nama = models.CharField(max_length=512)
    deskripsi = models.TextField()
    presentasi = models.TextField()
    usia = models.CharField(max_length=512)
    jadwal = models.TextField()
    dosis1 = models.TextField()
    dosis2 = models.TextField()

