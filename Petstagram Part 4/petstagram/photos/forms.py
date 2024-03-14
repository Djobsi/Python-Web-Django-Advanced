from django import forms

from petstagram.common.models import PhotoComment
from petstagram.photos.models import PetPhoto


class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        exclude = ['photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = PhotoComment
        fields = '__all__'
