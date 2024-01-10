import json

from django.contrib.auth.models import User

from rest_framework import serializers

class PositiveValueValidator:
    """
    Custom validator to ensure a positive value.
    """

    def __call__(self, value):
        if value <= 0:
            raise serializers.ValidationError("Value must be greater than 0.")


class StrongPasswordValidator:
    """
    Custom validator to ensure a strong password.
    """

    def __call__(self, value):
        if not any(char.isupper() for char in value) or not any(char.islower() for char in value) or not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")

positive_value_validator = PositiveValueValidator()
strong_password_validator = StrongPasswordValidator()