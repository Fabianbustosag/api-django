from rest_framework import serializers
from .models import Food, Image, Publication, UserData
from django.contrib.auth.models import User


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

class PublicationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Publication
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']