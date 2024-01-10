import json

from rest_framework import serializers

from api.models import Drawing, Shape, Annotation
from api.validators import positive_value_validator,strong_password_validator

class JSONFieldWithList(serializers.CharField):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        try:
            decoded_data = json.loads(data)
            if isinstance(decoded_data, list) and len(decoded_data) == 1:
                return decoded_data[0]
            return [data]
        except json.JSONDecodeError:
            return [data]

class LoginRequestSerializer(serializers.Serializer):
    """
    Serializer for handling login requests.
    """
    
    username = serializers.CharField()
    password = serializers.CharField(validators=[strong_password_validator])


class LoginResponseSerializer(serializers.Serializer):
    """
    Serializer for handling login responses.
    """

    token = serializers.CharField()
    expires = serializers.CharField()


class DrawingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Drawing model.
    """

    height = serializers.FloatField(validators=[positive_value_validator])
    width = serializers.FloatField(validators=[positive_value_validator])

    class Meta:
        model = Drawing
        fields = '__all__'


class ShapeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Shape model.
    """

    coordinates = JSONFieldWithList()
    dimensions = serializers.ListField(required=False)
    height = serializers.FloatField(validators=[positive_value_validator])
    width = serializers.FloatField(validators=[positive_value_validator])

    class Meta:
        model = Shape
        fields = '__all__'


class AnnotationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Annotation model.
    """
    position = JSONFieldWithList()

    class Meta:
        model = Annotation
        fields = '__all__'