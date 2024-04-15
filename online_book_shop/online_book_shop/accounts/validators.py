from django.core.exceptions import ValidationError


def is_upper_first_letter(value):
    if not value[0].isupper():
        raise ValidationError("Първата буква трябва да е главна!")
