from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from petstagram.core.models import IHaveUser

UserModel = get_user_model()


class Pet(IHaveUser, models.Model):
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
    )

    pet_photo = models.URLField(
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        editable=False,
    )

    # user = models.ForeignKey(UserModel,
    #                          on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)
