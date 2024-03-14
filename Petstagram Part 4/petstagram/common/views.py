from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import generic as views

from petstagram.common.forms import SearchForm
from petstagram.common.models import PhotoLike
from petstagram.photos.models import PetPhoto


# def index(request):
#     pet_name_pattern = request.GET.get('pet_name_pattern', default='')
#
#     pet_photos = PetPhoto.objects.all()
#
#     if pet_name_pattern:
#         pet_photos = pet_photos.filter(pets__name__icontains=pet_name_pattern)
#
#     search_form = SearchForm(request.GET)
#
#     if search_form.is_valid():
#         pet_photos = all_photos.filter(
#             pets__name__icontains=search_form.cleaned_data['pet_name'],
#         )
#
#     context = {
#         'pet_photos': pet_photos,
#         # 'search_form': search_form,
#         "pet_name_pattern": pet_name_pattern,
#     }
#
#     return render(request, 'common/home-page.html', context)


class IndexView(views.ListView):
    queryset = PetPhoto.objects.all() \
        .prefetch_related("pets") \
        .prefetch_related("photolike_set")

    template_name = "common/home-page.html"

    paginate_by = 1

    @property
    def pet_name_pattern(self):
        return self.request.GET.get('pet_name_pattern', None)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['pet_name_pattern'] = self.pet_name_pattern or ''

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        queryset = self.filter_by_pet_name_pattern(queryset)

        return queryset

    def filter_by_pet_name_pattern(self, queryset):
        pet_name_pattern = self.pet_name_pattern

        filter_query = {}

        if pet_name_pattern:
            filter_query["pets__name__icontains"] = pet_name_pattern

        return queryset.filter(**filter_query)


def like_pet_photo(request, pk):
    # pet_photo_like = PhotoLike.objects.first(pk=pk, user=request.user)
    pet_photo_like = PhotoLike.objects.filter(pet_photo_id=pk).first()

    if pet_photo_like:
        pet_photo_like.delete()
    else:
        PhotoLike.objects.create(pet_photo_id=pk)

    return redirect(request.META.get('HTTP_REFERER') + f"#photo-{pk}")















