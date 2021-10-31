from django.test import TestCase, Client
from django.db.models import Sum
from django.db.models.functions import Lower

from .models import Sebaran

# Create your tests here.

class SebaranIndexPageUnitTest(TestCase):
    def test_sebaran_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()
        
        response = Client().get('/sebaran/')
        
        self.assertQuerysetEqual(response.context[0]['sebaran'].all(), Sebaran.objects.all().order_by('-jumlah_kasus_aktif'))
    
    def test_sebaran_values_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()
        
        response = Client().get('/sebaran/')
        
        self.assertEqual(response.context[0]['sebaran_values'], str(list(Sebaran.objects.order_by('-jumlah_kasus_aktif').values())))
    
    def test_terkonfirmasi_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()

        response = Client().get('/sebaran/')
        self.assertEqual(response.context[0]['terkonfirmasi'], Sebaran.objects.aggregate(Sum('jumlah_kasus_terkonfirmasi'))['jumlah_kasus_terkonfirmasi__sum'])
    
    def test_aktif_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()

        response = Client().get('/sebaran/')
        self.assertEqual(response.context[0]['aktif'], Sebaran.objects.aggregate(Sum('jumlah_kasus_aktif'))['jumlah_kasus_aktif__sum'])
    
    def test_sembuh_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()

        response = Client().get('/sebaran/')
        self.assertEqual(response.context[0]['sembuh'], Sebaran.objects.aggregate(Sum('jumlah_sembuh'))['jumlah_sembuh__sum'])
    
    def test_meninggal_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()

        response = Client().get('/sebaran/')
        self.assertEqual(response.context[0]['meninggal'], Sebaran.objects.aggregate(Sum('jumlah_meninggal'))['jumlah_meninggal__sum'])

    def test_provinsi_data(self):
        # Populate Test Database
        Sebaran(provinsi='Jakarta', jumlah_kasus_terkonfirmasi=1, jumlah_kasus_aktif=2, jumlah_sembuh=3, jumlah_meninggal=4).save()
        Sebaran(provinsi='Bandung', jumlah_kasus_terkonfirmasi=10, jumlah_kasus_aktif=9, jumlah_sembuh=8, jumlah_meninggal=7).save()
        
        response = Client().get('/sebaran/')

        self.assertQuerysetEqual(response.context[0]['provinsi'].all(), Sebaran.objects.values('provinsi').order_by(Lower('provinsi')))
    
    def test_index_status_code(self):
        response = Client().get('/sebaran/')
        self.assertEqual(response.status_code, 200)