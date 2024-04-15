from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse

from django.views import generic as views

from online_book_shop.accounts.forms import BookShopUserCreationForm, CustomAuthenticationForm

from django.contrib.auth import views as auth_views, logout, login

from online_book_shop.accounts.models import Profile


class RegisterUserView(views.CreateView):
    template_name = "accounts/register_page.html"
    form_class = BookShopUserCreationForm
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, form.instance)
        return result


class LoginUserView(auth_views.LoginView):
    template_name = "accounts/login_page.html"
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm


def logout_user(request):
    logout(request)
    return redirect('home-page')


class DetailsUserView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/detail_page.html"

    def get_object(self, queryset=None):
        if not Profile.objects.all():
            return self.request.user

        user = self.request.user

        profile = Profile.objects.get_or_create(user=self.request.user)
        return profile


class UpdateUserView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_page.html"
    fields = ("first_name", "last_name", "age", "profile_picture")

    def get_success_url(self, **kwargs):
        return reverse(
            "details-page",
            kwargs={
                "pk": self.object.pk,
            }
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["age"].widget.attrs["placeholder"] = "Age"
        form.fields["first_name"].widget.attrs["placeholder"] = "First name"
        form.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        form.fields["profile_picture"].widget.attrs["placeholder"] = "Profile picture"

        return form

    def get_object(self, queryset=None):
        user = self.request.user
        profile, created = Profile.objects.get_or_create(user=user)

        return profile


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy("home-page")

    def get_object(self, queryset=None):
        return self.request.user


