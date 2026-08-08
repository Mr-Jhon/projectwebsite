from django.shortcuts import render
from .models import Artikel


def home(request):
    artikel = Artikel.objects.all().order_by('-tanggal_dibuat')

    return render(
        request,
        'core/home.html',
        {'artikel': artikel}
    )


def tentang(request):
    return render(request, 'core/tentang.html')


def kontak(request):
    return render(request, 'core/kontak.html')