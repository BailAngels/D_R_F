from django.contrib import admin

from homeworks.models import Fruits


@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
