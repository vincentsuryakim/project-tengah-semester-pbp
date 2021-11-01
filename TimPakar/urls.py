from django.urls import path
from .views import index

urlpatterns = [
    path('tim_pakar_covid_19', index, name='Tim Pakar Covid-19')
]