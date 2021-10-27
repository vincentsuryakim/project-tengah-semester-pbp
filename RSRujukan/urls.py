from django.urls import path
from .views import index, booking, book_user, create_rs, book_delete, updateUser

urlpatterns = [
    path('book/', booking, name='booking'),
    path('user_book/', book_user, name='user_book'),
    path('add_rs/', create_rs, name='add_rs'),
    path('book/<str:id>/', book_delete, name='book_delete'),
    path('update_data/', updateUser, name='update_data'),
    path('', index, name='rsrujukan'),
]