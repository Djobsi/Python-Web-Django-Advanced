from django.core.exceptions import ValidationError


def validate_title_min(value):
    if len(value) < 5:
        raise ValidationError("The title must be at least 5 characters long.")


def validate_author_min(value):
    if len(value) < 5:
        raise ValidationError("The author name must be at least 5 characters long.")
