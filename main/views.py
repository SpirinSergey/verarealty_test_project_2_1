from django.shortcuts import render
from django.shortcuts import render
from .models import Gallery
from .models import Listing
from django.http import HttpResponse


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
    gal_img = Gallery.objects.all()
    return render(request, 'main/gallery.html', context={'gal_img': gal_img})


def day(request):
    return render(request, 'main/day.html')


def night(request):
    return render(request, 'main/night.html')


def listings(request):
    listing_object = Listing.objects.all()
    return render(request, 'main/listings.html', context={'listing_object': listing_object})


def contact(request):
    return render(request, 'main/contact.html')




