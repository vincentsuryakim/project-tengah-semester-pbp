from django.urls import path
from .views import index, load_more2

urlpatterns = [
    path('', index, name="vaksincovid"),
    path('load-more2', load_more2, name='load-more2'),

]