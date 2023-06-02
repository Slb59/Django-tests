from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "role"]
    # list_filter = ["title", "time_created"]
    # search_fields = ["title", "description"]
    # ordering = ["user", "time_created"]
    # raw_id_fields = ["user"]
