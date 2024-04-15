from django.contrib import admin
from .models import Books


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price", "publication_date", "book_owner")
    list_filter = ("author", "publication_date")
    search_fields = ("title", "author")
    search_help_text = 'Заглавие или Автор'
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'author', 'price', 'publication_date', 'book_owner')
        }),
        ('Разширени Опции', {
            'classes': ('collapse',),
            'fields': ('description', 'genre')
        }),
    )

    actions = ['mark_as_published']