from django.urls import path, include

from petstagram.photos.views import CreatePetPhotoView, DetailPetPhotoView, EditPetPhotoView, delete_photo

urlpatterns = (
    path("create/", CreatePetPhotoView.as_view(), name="create-photo"),
    path(
        "<int:pk>/", include([
            path("", DetailPetPhotoView.as_view(), name="details-photo"),
            path("edit/", EditPetPhotoView.as_view(), name="edit-photo"),
            path('delete/', delete_photo, name='delete-photo')
        ]),
    ),
)
