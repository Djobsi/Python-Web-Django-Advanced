from django.core import exceptions
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixin

from petstagram.pets.forms import PetCreateForm, PetEditForm, PetDeleteForm
from petstagram.pets.models import Pet

from petstagram.accounts.views import OwnerRequiredMixin


# CBV
class CreatePetView(auth_mixin.LoginRequiredMixin, views.CreateView):
    # model = Pet
    form_class = PetCreateForm
    template_name = "pets/create-pet.html"

    def get_success_url(self):
        return reverse("details-pet", kwargs={
            "username": "Aleks",
            "pet_slug": self.object.slug,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user
        return form 


# FBV
# def create_pet(request):
#     pet_form = PetCreateForm(request.POST or None)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             created_pet = pet_form.save()
#             return redirect('details-pet', username='aleks', pet_slug=created_pet.slug)
#
#     context = {
#         'pet_form': pet_form,
#     }
#
#     return render(request, 'pets/create-pet.html', context)


# class OwnerRequiredMixin:
#     def dispatch(self, request, *args, **kwargs):
#         pass


# CBV
class EditPetView(OwnerRequiredMixin, views.UpdateView):
    model = Pet
    template_name = "pets/edit-pet.html"
    form_class = PetEditForm
    slug_url_kwarg = "pet_slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "username"

        return context

    def get_success_url(self):
        return reverse("details-pet", kwargs={
            "username": self.request.GET.get("username"),
            "pet_slug": self.object.slug,
        })


# FBV
# def edit_pet(request, username, pet_slug):
#     pet = Pet.objects.filter(slug=pet_slug) \
#         .get()
#
#     pet_form = PetEditForm(request.POST or None, instance=pet)
#
#     if request.method == 'POST':
#         if pet_form.is_valid():
#             pet_form.save()
#             return redirect('details-pet', username=username, pet_slug=pet_slug)
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, 'pets/edit-pet.html', context)


# CBV
class DetailPetView(auth_mixin.LoginRequiredMixin, views.DetailView):
    template_name = "pets/details-pet.html"
    slug_url_kwarg = "pet_slug"

    queryset = Pet.objects.all() \
        .prefetch_related("petphoto_set") \
        .prefetch_related("petphoto_set__photolike_set") \
        .prefetch_related("petphoto_set__pets")


# FBV
# def details_pet(request, username, pet_slug):
#     context = {
#         'pet': Pet.objects.get(slug=pet_slug)
#     }
#
#     return render(request, 'pets/details-pet.html', context)


# CBV
class DeletePetView(OwnerRequiredMixin, auth_mixin.LoginRequiredMixin, views.DeleteView):
    model = Pet
    template_name = "pets/delete-pet.html"
    slug_url_kwarg = "pet_slug"
    form_class = PetDeleteForm

    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["username"] = "username"

        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs


# FBV
# def delete_pet(request, username, pet_slug):
#     pet = Pet.objects.get(slug=pet_slug)
#
#     pet_form = PetDeleteForm(request.POST or None, instance=pet)
#
#     if request.method == "POST":
#         pet_form.save()
#         return redirect("index")
#
#     context = {
#         "pet_form": pet_form,
#         "username": username,
#         "pet": pet,
#     }
#
#     return render(request, "pets/delete-pet.html", context)


