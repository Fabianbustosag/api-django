from django.shortcuts import render
from django.http import HttpResponse
from ..forms import MyModelForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ImageUploadSerializer

import requests
import json

from .procesing_image import *
from ..models import Food 

# Recivo un diccionario para crear la instacia de food en la base de datos
def create_product_in_db(product_data: dict):
    try:
        product = Food.objects.create(
            food_name=product_data['food_name'],
            category=product_data['category'],
            food_amount_g=product_data['food_amount_g'],
            img_src=product_data['img_src']
        )
        return product
    except Exception as e:
        return f"An error occurred while saving to the database: {e}"

# Funcion para subir una imagen al servidor, mediante una plantilla html 
def upload_image(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Imagen subida con éxito')
    else:
        form = MyModelForm()
    return render(request, 'upload_image.html', {'form': form})


def func_to_get_values():
    # tomo la ruta de la imagen
    # text = get_text_from_image() extraigo el texto de la imagen
    # con el texto extraigo los codigos
    # con los codigos pregunto a la API (OpenFoodFacts)
    # crear un producto con los valores devueltos

    pass

# Clase para subir una imagen al servidor mediante API REST
class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            # Si la respiesta es valida se muestra la respuesta como json: "image": "/media/media/only_code.jpg"
            func_to_get_values() # se hace que se evalue la imagen / serializer.data 
            # print(f'serializeer.data: {serializer.data}')
            path_image = serializer.data.get('image') # ruta donde quedo almacenada la imagen
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   
