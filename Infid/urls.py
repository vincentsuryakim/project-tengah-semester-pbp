from django.urls import path
from .views import index, loginFunction

urlpatterns = [
    path('', index, name='index'),
    path('', loginFunction),
]
