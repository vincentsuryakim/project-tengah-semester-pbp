from django.urls import path
from .views import index, edit_sebaran, edit_user, edit_existing_user, delete_user

urlpatterns = [
    path('', index, name='index'),
    path('edit', edit_sebaran, name='edit_sebaran'),
    path('edit-user', edit_user, name='edit_user'),
    path('edit-existing-user', edit_existing_user, name='edit_existing_user'),
    path('delete-user', delete_user, name='delete_user'),
]
