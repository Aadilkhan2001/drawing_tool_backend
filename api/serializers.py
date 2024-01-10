from rest_framework import serializers

from api.models import Drawing, Shape, Annotation
from api.validators import (PositiveValueValidator,
                            UsernameValueValidator,
                            StrongPasswordValidator,
                            JSONFieldValidator,)


class LoginRequestSerializer(serializers.Serializer):
    """
    Serializer for handling login requests.
    """
    
    username = serializers.CharField(validators=[UsernameValueValidator])
    password = serializers.CharField(validators=[StrongPasswordValidator])


class LoginResponseSerializer(serializers.Serializer):
    """
    Serializer for handling login responses.
    """

    token = serializers.CharField()
    expires = serializers.CharField()


class DrawingSerializer(serializers.Serializer):
    """
    Serializer for the Drawing model.
    """

    height = serializers.FloatField(validators=[PositiveValueValidator])
    width = serializers.FloatField(validators=[PositiveValueValidator])

    class Meta:
        model = Drawing
        fields = '__all__'


class ShapeSerializer(serializers.Serializer):
    """
    Serializer for the Shape model.
    """

    coordinates = serializers.CharField(validators=[JSONFieldValidator])
    dimensions = serializers.CharField(validators=[JSONFieldValidator], blank=True, null=True,)
    height = serializers.FloatField(validators=[PositiveValueValidator])
    width = serializers.FloatField(validators=[PositiveValueValidator])

    class Meta:
        model = Shape
        fields = '__all__'


class AnnotationSerializer(serializers.Serializer):
    """
    Serializer for the Annotation model.
    """
    position = serializers.CharField(validators=[JSONFieldValidator])

    class Meta:
        model = Annotation
        fields = '__all__'