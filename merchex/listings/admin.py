from django.contrib import admin
from listings.models import Band, Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')


class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    # liste les champs que nous voulons sur l'affichage de la liste
    list_display = ('name', 'year_formed', 'genre')


# nous modifions cette ligne, en ajoutant un deuxième argument
admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)
