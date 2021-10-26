from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class RumahSakit(models.Model):
    pilihanTempat = (
        ('Sumatera', 'Sumatera'),
        ('Jakarta', 'DKI Jakarta'),
        ('Banten', 'Banten'),
        ('Bali', 'Bali'),
        ('Nusa Tenggara', 'Nusa Tenggara'),
        ('Kalimantan', 'Kalimantan'),
        ('Sulawesi', 'Sulawesi'),
        ('Maluku', 'Maluku'),
        ('Papua', 'Papua')
    )
    nama = models.CharField(max_length=100)
    tempat = models.CharField(max_length=15, choices=pilihanTempat)
    alamat = models.TextField(max_length=300)
    no_telfon = models.CharField(max_length=14)

    def __str__(self):
        return self.nama

class BookingRS(models.Model):
    nama = models.CharField(max_length=40)
    umur = models.IntegerField()
    noTelfon = models.CharField(max_length=13)
    rumahSakit = models.ForeignKey(RumahSakit, on_delete=CASCADE)

    def __str__(self):
        return f"{self.nama} booking di {self.rumahSakit}"