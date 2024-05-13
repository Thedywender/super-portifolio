from django.core.exceptions import ValidationError


def validate_not_empty(value):
    if not value:
        raise ValidationError("Este campo não pode ser vazio.")


def validate_max_length(value):
    if len(value) > 500:
        raise ValidationError(
            "Este campo não pode ter mais de 500 caracteres."
        )
