from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, BaseValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size


UserModel = get_user_model()


def random_validator(value):
    # If invalid, `raise ValidationError`
    # Else, if valid, do nothing
    pass


SIZE_5_MB = 5 * 1024 * 1024


class MaxFileSizeValidator(BaseValidator):
    def clean(self, x):
        return x.size

    def compare(self, file_size, max_size):
        return max_size < file_size


class PetPhoto(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    photo = models.ImageField(
        upload_to='pet_photos/',
        blank=False,
        null=False,
        validators=[
            validate_file_size
        ]
    )

    description = models.TextField(
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        )
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    user = models.ForeignKey(UserModel,
                             on_delete=models.RESTRICT)
