from django.urls import path
from . import views

app_name = "listings"
urlpatterns = [
    path("bands/", views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path("listings/", views.listings),
    path("about_us/", views.about),
]
