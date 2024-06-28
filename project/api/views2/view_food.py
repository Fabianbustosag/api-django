from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import FoodSerializer
from ..models import Food

class FoodModelView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

def algo():
    pass