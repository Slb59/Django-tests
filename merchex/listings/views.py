# from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()

    return render(request, "listings/band_list.html",
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band}
                  )  # nous passons l'id au modèle


def listings(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing.html",
                  {'listings': listings})


def about(request):
    return render(request, 'listings/about.html')
