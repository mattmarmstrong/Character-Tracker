from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.regPage, name="registration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name="home"),

    path('room/<str:pk>/', views.room, name="room"),

    path('create-sheet/', views.create_sheet, name="create-sheet"),
    path('update-sheet/<str:pk>/', views.update_sheet, name="update-sheet"),
    path('delete-sheet/<str:pk>/', views.delete_sheet, name="delete-sheet"),

    path('sheet/<str:pk>/', views.sheet, name="sheet"),
    path('glossary/', views.glossary, name="glossary"),
]
