from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboardView, name='dashboard'),
]
