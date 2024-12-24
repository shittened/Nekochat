from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name = 'rooms'),
    path('<slug:slug>/', views.room, name = 'room'),
    #path('delete-message/<int:pk>/', views.deleteMessage, name = 'delete-message'),
    path('delete-message/<message_id>', views.deleteMessage, name = 'delete-message'),
]
