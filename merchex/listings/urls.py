from django.urls import path
from . import views

app_name = "listings"
urlpatterns = [
    path("bands/", views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),
    path('bands/add/', views.band_create, name='band-create'),
    path("listings/", views.listings, name='listings'),
    path("about_us/", views.about, name='about-us'),
    path('contact-us/', views.contact, name='contact'),
    path('email-sent/', views.email_sent, name='email-sent'),
]
