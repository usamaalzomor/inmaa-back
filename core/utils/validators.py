from django.core.exceptions import ValidationError

def validate_boundary(value):
    if not value.valid:
        raise ValidationError("Invalid geometry")