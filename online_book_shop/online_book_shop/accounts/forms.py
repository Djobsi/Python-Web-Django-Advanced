from django.contrib.auth import forms as auth_forms, get_user_model

from online_book_shop.accounts.models import BookShopUser, Profile

from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class BookShopUserCreationForm(auth_forms.UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = BookShopUser
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)

        return self.user


class BookShopChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = _('Email')