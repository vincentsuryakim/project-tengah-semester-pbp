from django.urls import path
from .views import index, sebaran_json, add_sebaran, edit_sebaran, edit_user, edit_existing_user, delete_user, sebaran_json

urlpatterns = [
    path('', index, name='index'),
    path('sebaran-json', sebaran_json, name='sebaran_json'),
    path('add-sebaran', add_sebaran, name='add_sebaran'),
    path('edit', edit_sebaran, name='edit_sebaran'),
    path('edit-user', edit_user, name='edit_user'),
    path('edit-existing-user', edit_existing_user, name='edit_existing_user'),
    path('delete-user', delete_user, name='delete_user'),
]
