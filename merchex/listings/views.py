from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def hello(request):
    bands = Band.objects.all()

    return render(request, "listings/hello.html",
                  {'bands': bands})


def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html",
                  {'listings': listings})


def about(request):
    return render(request, 'listings/about.html')
