from django.urls import path
from . import views

app_name = 'tutodjango'

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
]
