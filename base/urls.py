from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('create-sheet/', views.createSheet, name="create-sheet"),
    path('update-sheet/', views.updateSheet, name="update-sheet"),
    path('sheet/<str:pk>/', views.sheet, name="sheet"),
]

