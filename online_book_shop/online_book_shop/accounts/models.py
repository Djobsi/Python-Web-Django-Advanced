from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from online_book_shop.accounts.managers import BookShopUserManager
from online_book_shop.accounts.validators import is_upper_first_letter
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class BookShopUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(
        _("date_joined"),
        default=timezone.now
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = BookShopUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        related_name='bookshop_users_groups',
        related_query_name='bookshop_user_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        related_name='bookshop_users_permissions',
        related_query_name='bookshop_user_permission',
    )


class Profile(models.Model):
    MAX_LENGTH_FIRST_NAME = 10
    MAX_LENGTH_LAST_NAME = 10

    MAX_AGE = 99
    MIN_AGE = 16

    first_name = models.CharField(
        max_length=MAX_LENGTH_FIRST_NAME,
        null=False,
        blank=False,
        validators=[
            is_upper_first_letter,
        ],
        verbose_name="Име",
    )

    last_name = models.CharField(
        max_length=MAX_LENGTH_LAST_NAME,
        null=False,
        blank=False,
        validators=[
            is_upper_first_letter,
        ],
        verbose_name="Фамилия"
    )

    age = models.IntegerField(
        validators=[
            MaxValueValidator(MAX_AGE),
            MinValueValidator(MIN_AGE),
        ],
        null=True,
        blank=True,
        verbose_name="Години"
    )

    profile_money = models.FloatField(
        null=False,
        blank=False,
        default=200,
        verbose_name="Пари"
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
        verbose_name="Профилна снимка"
    )

    user = models.OneToOneField(
        BookShopUser,
        primary_key=True,
        on_delete=models.CASCADE,
        verbose_name="Потребител"
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name


