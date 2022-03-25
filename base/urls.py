from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.reg_page, name="registration"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name="home"),

    path('room/<str:pk>/', views.room, name="room"),

    path('profile/', views.user_profile, name="user-profile"),

    path('create-sheet/', views.create_sheet, name="create-sheet"),
    path('update-sheet/<str:pk>/', views.update_sheet, name="update-sheet"),
    path('delete-sheet/<str:pk>/', views.delete_sheet, name="delete-sheet"),

    path('sheet/<str:pk>/', views.sheet, name="sheet"),
    path('glossary/', views.glossary, name="glossary"),

    path('rate-options/', views.rate_options, name="rate-options"),
    path('feat/<str:pk>/', views.feat, name="feat"),
    path('rate/<str:pk>/', views.rate, name="rate-feat"),
]
