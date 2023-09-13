from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('editprofile/', views.editprofileView, name='editprofile'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('logout/', views.logoutView, name='logout'),
]
