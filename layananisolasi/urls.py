from django.urls import path
from .views import index,load_more

urlpatterns = [
    path('', index, name='layananisolasi'),
    path('load-more',load_more,name='load-more'),
]