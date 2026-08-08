from django.contrib import admin
from .models import Artikel


@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'tanggal_dibuat')
    search_fields = ('judul', 'isi')