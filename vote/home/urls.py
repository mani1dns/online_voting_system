from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('editprofile/', views.editprofileView, name='editprofile'),
    path('changepass/', views.changePasswordView, name='changepass'),
    path('logout/', views.logoutView, name='logout'),
    path('result/', views.resultView, name='result'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('position/', views.positionView, name='position'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Online Voting System"
admin.site.index_title = "Welcome to online voting system admin panel"
admin.site.site_title = "OVS"

