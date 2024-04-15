from django import forms

from online_book_shop.web.models import AnonymousUsers


class ContactForm(forms.ModelForm):
    class Meta:
        model = AnonymousUsers
        fields = "__all__"
