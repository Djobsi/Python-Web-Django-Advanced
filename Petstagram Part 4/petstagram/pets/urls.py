from django.urls import path, include

from petstagram.pets.views import CreatePetView, DetailPetView, DeletePetView, EditPetView

urlpatterns = (
    path("create/", CreatePetView.as_view(), name="create-pet"),
    path("<str:username>/pet/<slug:pet_slug>/", include([
        path("", DetailPetView.as_view(), name="details-pet"),
        path("edit/", EditPetView.as_view(), name="edit-pet"),
        path("delete/", DeletePetView.as_view(), name="delete-pet"),
    ]))
)
