from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import render, redirect

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse

from django.views import generic as views

from petstagram.accounts.forms import PetstagramUserCreationForm
from petstagram.accounts.models import Profile


class OwnerRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(auth_views.LoginView):
    template_name = "accounts/signin-page.html"
    redirect_authenticated_user = True


class SignUpUserView(views.CreateView):
    template_name = "accounts/signup-page.html"
    form_class = PetstagramUserCreationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, form.instance)

        return result


def signout_user(request):
    logout(request)
    return redirect('index')


class ProfileDetailsView(OwnerRequiredMixin, views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/details-profile.html"


class EditProfileView(views.UpdateView):
    queryset = Profile.objects.all()
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")
    template_name = "accounts/edit-profile.html"

    def get_success_url(self, **kwargs):
        return reverse(
            "details-profile",
            kwargs={
                "pk": self.object.pk,
            }
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["date_of_birth"].widget.attrs["placeholder"] = "Date of birth"
        form.fields["first_name"].widget.attrs["placeholder"] = "First name"
        form.fields["last_name"].widget.attrs["placeholder"] = "Last name"
        form.fields["profile_picture"].widget.attrs["placeholder"] = "Profile picture"

        form.fields["date_of_birth"].widget.attrs["type"] = "date"
        form.fields["date_of_birth"].label = "Birthday"
        return form


class DeleteProfileView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete-profile.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
