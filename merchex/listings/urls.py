from django.urls import path
from . import views

app_name = "listings"
urlpatterns = [
    path("hello/", views.hello),
    path("listings/", views.listings),
    path("about_us/", views.about),
]
