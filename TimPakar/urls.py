from django.urls import path
from .views import index, add_regist, more_pakar

urlpatterns = [
    path('', index, name="timPakarCovid"),
    path('daftar-timPakar', add_regist, name="daftar-timPakar"),
    path('more-pakar', more_pakar, name='more_pakar'),

]