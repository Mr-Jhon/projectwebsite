from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def tentang(request):
    return render(request, 'core/tentang.html')


def kontak(request):
    return render(request, 'core/kontak.html')