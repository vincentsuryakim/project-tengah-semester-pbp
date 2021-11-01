from django.urls import path
from .views import index, add_regist, load_more

urlpatterns = [
    path('', index, name="timPakarCovid"),
    path('daftar-timPakar', add_regist, name="daftar-timPakar"),
    path('load-more', load_more, name='load-more'),

]