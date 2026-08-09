from django.shortcuts import get_object_or_404, render
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


def daftar_artikel(request):
    artikel = Artikel.objects.all().order_by('-tanggal_dibuat')

    return render(
        request,
        'core/daftar_artikel.html',
        {'artikel': artikel}
    )


def detail_artikel(request, id):
    artikel = get_object_or_404(Artikel, id=id)

    return render(
        request,
        'core/detail_artikel.html',
        {'artikel': artikel}
    )