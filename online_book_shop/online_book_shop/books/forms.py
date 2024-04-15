from django import forms

from online_book_shop.books.models import Books
from django.utils import timezone


class BaseClassBooksForm(forms.ModelForm):

    class Meta:
        model = Books
        exclude = ('book_owner', )

        widgets = {
            'cover': forms.URLInput(
                attrs={'placeholder': "https://..."}
            )
        }

        error_messages = {
            'cover': {
                'unique': "This image URL is already in use! Provide a new one.",
            }
        }


class BooksForm(BaseClassBooksForm):
    pass


class DeleteBookForm(forms.ModelForm):
    class Meta:
        model = Books
        exclude = ('book_owner', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set all fields as disabled
        for field in self.fields.values():
            field.disabled = True

