from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def developers(request):
    return render(request, 'main/developers.html')


def inside(request):
    return render(request, 'main/inside.html')


def outside(request):
    return render(request, 'main/outside.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def day(request):
    return render(request, 'main/day.html')


def night(request):
    return render(request, 'main/night.html')


def listings(request):
    return render(request, 'main/listings.html')


def contact(request):
    return render(request, 'main/contact.html')


