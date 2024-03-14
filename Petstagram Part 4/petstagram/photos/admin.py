from django.contrib import admin

from petstagram.photos.models import PetPhoto


@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_of_publication', 'location', 'description', 'get_tagged_pets')

    @staticmethod
    def get_tagged_pets(obj):
        return ', '.join([pet.name for pet in obj.pets.all()])
