from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic as views

from django.contrib.auth import mixins as auth_mixin

from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm, CommentForm
from petstagram.photos.models import PetPhoto

from petstagram.accounts.views import OwnerRequiredMixin


# CBV
class CreatePetPhotoView(auth_mixin.LoginRequiredMixin, views.CreateView):
    template_name = "photos/create-photo.html"
    form_class = PhotoCreateForm
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets")

    def get_success_url(self):
        return reverse("details-photo", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.instance.user = self.request.user

        return form


# FBV
# def create_photo(request):
#     photo_form = PhotoCreateForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if photo_form.is_valid():
#             created_photo = photo_form.save()
#             return redirect('details-photo', pk=created_photo.pk)
#
#     context = {
#         'create_form': photo_form,
#     }
#
#     return render(request, 'photos/create-photo.html', context)


# CBV
class DetailPetPhotoView(auth_mixin.LoginRequiredMixin, views.DetailView):
    model = PetPhoto
    template_name = "photos/photo-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["pk"] = self.object.pk

        return context


# FBV
# def photo_details(request, pk):
#     context = {
#         'pet_photo': PetPhoto.objects.get(pk=pk)
#     }
#
#     return render(request, 'photos/photo-details.html', context)


# CBV
class EditPetPhotoView(OwnerRequiredMixin, views.UpdateView):
    model = PetPhoto
    form_class = PhotoEditForm
    template_name = "photos/photo-edit.html"

    def get_success_url(self):
        return reverse("details-photo", kwargs={
            "pk": self.object.pk,
        })


# FBV
# def edit_photo(request, pk):
#     photo = PetPhoto.objects.filter(pk=pk).get()
#
#     photo_form = PhotoEditForm(request.POST or None, instance=photo)
#
#     if request.method == "POST":
#         if photo_form.is_valid():
#             photo_form.save()
#             return redirect('details-photo', pk=pk)
#     context = {
#         "photo_form": photo_form,
#         "pk": pk,
#     }
#
#     return render(request, 'photos/photo-edit.html', context)


# FBV
def delete_photo(request, pk):
    photo = PetPhoto.objects.get(pk=pk)
    photo.delete()
    return redirect('index')


def add_comment(request, photo_id):
    if request.method == "POST":
        photo = PetPhoto.objects.get(id=photo_id)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_photo = photo
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTPP_REFERER'] + f'#{photo_id}')
