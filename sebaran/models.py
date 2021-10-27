from django.conf import settings
from django.db import models

# Create your models here.

class Sebaran(models.Model):
    provinsi = models.CharField(max_length=64, unique=True)
    jumlah_kasus_terkonfirmasi = models.IntegerField()
    jumlah_kasus_aktif = models.IntegerField()
    jumlah_sembuh = models.IntegerField()
    jumlah_meninggal = models.IntegerField()

    def __str__(self):
        return self.provinsi
    

class SebaranUser(models.Model):
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    provinsi = models.ForeignKey(Sebaran, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_id} - {self.provinsi}'