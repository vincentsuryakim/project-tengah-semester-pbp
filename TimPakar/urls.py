from django.urls import path
from .views import index, add_regist, more_pakar, search_json, add_from_flutter

urlpatterns = [
    path('', index, name="timPakarCovid"),
    path('daftar-timPakar', add_regist, name="daftar-timPakar"),
    path('more-pakar', more_pakar, name='more_pakar'),
    path('search-json', search_json, name='search_json'),
    path('add-from-flutter', add_from_flutter, name='add_from_flutter')
]