# import unicodedata
# from django import forms
# from django.contrib.auth import password_validation
# # from django.contrib.auth.forms import UsernameField
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
#
#
# class PetstagramUsernameField(forms.CharField):
#     def to_python(self, value):
#         value = super().to_python(value)
#         if self.max_length is not None and len(value) > self.max_length:
#             return value
#         return unicodedata.normalize("NFKC", value)
#
#     def widget_attrs(self, widget):
#         return {
#             **super().widget_attrs(widget),
#             "autocapitalize": "none",
#             "autocomplete": "username",
#             "placeholder": "Enter email",
#         }
#
#
# class BasePetstagramUserCreationForm(forms.ModelForm):
#
#     error_messages = {
#         "password_mismatch": _("The two password fields didn’t match."),
#     }
#
#     password1 = forms.CharField(
#         label=_("Password"),
#         strip=False,
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Enter password"}),
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password confirmation"),
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password", "placeholder": "Enter password again"}),
#         strip=False,
#     )
#
#     class Meta:
#         model = User
#         fields = ("username",)
#         field_classes = {"username": PetstagramUsernameField}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if self._meta.model.USERNAME_FIELD in self.fields:
#             self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
#                 "autofocus"
#             ] = True
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(
#                 self.error_messages["password_mismatch"],
#                 code="password_mismatch",
#             )
#         return password2
#
#     def _post_clean(self):
#         super()._post_clean()
#         # Validate the password after self.instance is updated with form data
#         # by super().
#         password = self.cleaned_data.get("password2")
#         if password:
#             try:
#                 password_validation.validate_password(password, self.instance)
#             except ValidationError as error:
#                 self.add_error("password2", error)
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#             if hasattr(self, "save_m2m"):
#                 self.save_m2m()
#         return user
#
#
# class PetstagramUserCreationForm(BasePetstagramUserCreationForm):
#     def clean_username(self):
#         username = self.cleaned_data.get("username")
#         if (
#             username
#             and self._meta.model.objects.filter(username__iexact=username).exists()
#         ):
#             self._update_errors(
#                 ValidationError(
#                     {
#                         "username": self.instance.unique_error_message(
#                             self._meta.model, ["username"]
#                         )
#                     }
#                 )
#             )
#         else:
#             return username
