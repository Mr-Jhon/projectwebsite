from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('tentang/', views.tentang, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),
]