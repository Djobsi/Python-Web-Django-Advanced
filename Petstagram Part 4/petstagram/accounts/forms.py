from django.contrib.auth import forms as auth_forms, get_user_model

import petstagram.accounts.base_forms
from petstagram.accounts.models import PetstagramUser

UserModel = get_user_model()


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = PetstagramUser
        fields = ('email',)

    def save(self, *args, **kwargs):
        self.user = super().save(*args, **kwargs)

        return self.user


class PetstagramChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
