from rest_framework import serializers
from .models import Food


# el __all__ debe ser quitado por cosas de seguridad y solo poner los metodos necesarios
class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = '__all__'
