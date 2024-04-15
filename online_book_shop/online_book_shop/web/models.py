from django.core.validators import MinLengthValidator
from django.db import models


class AnonymousUsers(models.Model):
    MAX_LENGTH_DESC = 250
    MIN_LENGTH_DESC = 10

    MAX_LENGTH_NAME = 20
    MIN_LENGTH_NAME = 3

    your_name = models.CharField(
        max_length=MAX_LENGTH_NAME,
        validators=[MinLengthValidator(MIN_LENGTH_NAME)],
        null=False,
        blank=False,
        verbose_name="Your name:"
    )

    from_email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
        verbose_name="Your email address:"
    )

    message = models.TextField(
        max_length=MAX_LENGTH_DESC,
        validators=[
            MinLengthValidator(MIN_LENGTH_DESC),
        ],
        null=False,
        blank=False,
        verbose_name="Your message:"
    )
