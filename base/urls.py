from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.regPage, name="registration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name="home"),

    path('room/<str:pk>/', views.room, name="room"),
    path('profile/<str:pk>/', views.userProfile, name = "user-profile"),
    path('create-sheet/', views.createSheet, name="create-sheet"),
    path('update-sheet/<str:pk>/', views.updateSheet, name="update-sheet"),
    path('delete-sheet/<str:pk>/', views.deleteSheet, name="delete-sheet"),
    path('sheet/<str:pk>/', views.sheet, name="sheet"),
]
