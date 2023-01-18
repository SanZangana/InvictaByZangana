from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_list, name='get_todo_list'), 
    path('add/', views.add_item, name='add_item'),
    path('edit/<item_id>/', views.edit_item, name='edit'),
    path('toggle/<item_id>/', views.toggle_item, name='toggle'),
    path('delete/<item_id>/', views.delete_item, name='delete'),
]
