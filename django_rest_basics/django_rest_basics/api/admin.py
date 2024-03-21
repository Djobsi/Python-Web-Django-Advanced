from django.contrib import admin

from django_rest_basics.api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "genre")
