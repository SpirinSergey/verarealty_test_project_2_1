from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('developers', views.developers, name='developers'),
    path('inside', views.inside, name='inside'),
    path('outside', views.outside, name='outside'),
    path('gallery', views.gallery, name='gallery'),
    path('day', views.day, name='day'),
    path('night', views.night, name='night'),
    path('listings', views.listings, name='listings'),
    path('contact', views.contact, name='contact'),
    ]