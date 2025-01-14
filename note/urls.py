from django.urls import path
from . import views

urlpatterns = [
    path('', views.all, name='all'),
    path('delete/<int:note_id>', views.delete_note, name='delete'),
    path('create', views.create_note, name='create'),
    path('edit/<int:note_id>', views.edit_note, name='edit'),

]   