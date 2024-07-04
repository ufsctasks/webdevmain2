from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.sobre, name='sobre'),
    path('eventos/', views.eventos, name='eventos'),
    path('guia/', views.guia, name='guia'),
    path('prj/', views.prj, name='prj'),
    path('voluntariado/', views.voluntariado, name='voluntariado'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('recovery/', views.recovery, name='recovery'),
    path('test_500_view/', views.test_500_view, name='test_500_view'),
    path('custom_404_view', views.custom_404_view, name='custom_404_view'),
    path('prj/<int:projeto_id>/', views.projeto_detail, name='projetos_detail'),
]

handler404 = 'tsfApp.views.custom_404_view'
