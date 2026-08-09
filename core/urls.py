from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('tentang/', views.tentang, name='tentang'),

    path('kontak/', views.kontak, name='kontak'),

    path('artikel/', views.daftar_artikel, name='daftar_artikel'),

    path(
        'artikel/<int:id>/',
        views.detail_artikel,
        name='detail_artikel'
    ),
]