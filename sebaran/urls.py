from django.urls import path
from .views import index, sebaran_json, edit_sebaran, edit_user, edit_existing_user, delete_user, sebaran_json

urlpatterns = [
    path('', index, name='index'),
    path('sebaran-json', sebaran_json, name='sebaran_json'),
    path('edit', edit_sebaran, name='edit_sebaran'),
    path('edit-user', edit_user, name='edit_user'),
    path('edit-existing-user', edit_existing_user, name='edit_existing_user'),
    path('delete-user', delete_user, name='delete_user'),
]
