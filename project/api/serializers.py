from rest_framework import serializers
from .models import Food, Image


# el __all__ debe ser quitado por cosas de seguridad y solo poner los metodos necesarios
class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = '__all__'

# serializer de el modelo image
class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']