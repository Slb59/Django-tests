from django.contrib import admin
from .models import Photo, Blog, BlogContributor


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ["caption", "uploader", "date_created"]
    list_filter = ["caption", "date_created"]
    search_fields = ["caption", "uploader"]
    ordering = ["date_created"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "starred", "date_created"]
    list_filter = ["title", "date_created"]
    search_fields = ["title", "content"]
    ordering = ["date_created"]


@admin.register(BlogContributor)
class BlogContributorAdmin(admin.ModelAdmin):
    list_display = ["contributor", "blog", "contribution"]
