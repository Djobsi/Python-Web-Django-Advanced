from django.db import models

from online_book_shop.accounts.models import BookShopUser
from online_book_shop.books.validators import validate_title_min, validate_author_min

from datetime import datetime


class Genre(models.TextChoices):
    FICTION = 'Fiction', 'Fiction'
    MYSTERY = 'Mystery', 'Mystery'
    THRILLER = 'Thriller', 'Thriller'
    ROMANCE = 'Romance', 'Romance'
    FANTASY = 'Fantasy', 'Fantasy'
    HORROR = 'Horror', 'Horror'
    DRAMA = 'Drama', 'Drama'
    COMEDY = 'Comedy', 'Comedy'
    ACTION = 'Action', 'Action'
    CRIME = 'Crime', 'Crime'
    WESTERN = 'Western', 'Western'
    AUTOBIOGRAPHY = 'Autobiography', 'Autobiography'


class Books(models.Model):
    MAX_TITLE_LENGTH = 30

    MAX_AUTHOR_LENGTH = 30

    MAX_DESCRIPTION_LENGTH = 200

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=[validate_title_min],
        null=False,
        blank=False,
        verbose_name="Заглавие"
    )

    author = models.CharField(
        max_length=MAX_AUTHOR_LENGTH,
        validators=[validate_author_min],
        null=False,
        blank=False,
        verbose_name="Автор"
    )

    description = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        verbose_name="Описание"
    )

    price = models.FloatField(
        null=False,
        blank=False,
        default=20,
        verbose_name="Цена"
    )

    publication_date = models.DateTimeField(
        default=datetime.now,
        verbose_name="Дата на публикуване"
    )

    genre = models.CharField(
        max_length=max(len(book) for _, book in Genre.choices),
        choices=Genre.choices,
        null=False,
        blank=False,
        verbose_name="Жанр"
    )

    cover = models.URLField(
        unique=True,
        null=False,
        blank=False,
        error_messages={'unique': "This image URL is already in use! Provide a new one."},
        verbose_name='Image URL'
    )

    book_owner = models.ForeignKey(
        BookShopUser,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )


class ShoppingCart(models.Model):
    user = models.OneToOneField(BookShopUser, on_delete=models.CASCADE)
    books = models.ManyToManyField(Books)


