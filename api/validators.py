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

class UsernameValueValidator:
    """
    Custom validator to ensure a username is unique.
    """

    def __call__(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already in use.")
        

class StrongPasswordValidator:
    """
    Custom validator to ensure a strong password.
    """

    def __call__(self, value):
        if not any(char.isupper() for char in value) or not any(char.islower() for char in value) or not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")


class JSONFieldValidator:
    """
    Custom validator to ensure data is in JSON format.
    """

    def __call__(self, value):
        try:
            json.loads(value)
        except json.JSONDecodeError:
            raise serializers.ValidationError("Invalid JSON format. Data should be a valid JSON.")