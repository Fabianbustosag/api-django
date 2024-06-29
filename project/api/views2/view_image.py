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
from ..models import Food , UserData

from django.conf import settings

# from ...media import 

# Recivo un diccionario para crear la instacia de food en la base de datos
def create_product_from_dict(product_data: dict):
    user = UserData.objects.get(pk=1)
    try:
        print('create_product')
        print('product: ', product_data)
        product = Food.objects.create(
            user = user,
            food_name = product_data['food_name'], # str
            # category = product_data['category'], # str
            food_amount_g = limpiar_y_convertir(product_data['food_amount_g']), # Float
            img_src = product_data['img_src'] # str
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

# funcion que deberia printear lo lo creado
def func_to_get_values(path_image: str):
    # tomo la ruta de la imagen
    text = get_text_from_image(path_image) # extraigo el texto de la imagen
    print(f'texto: {text}')
    # con el texto extraigo los codigos
    lineas = text.splitlines()
    i=0
    for linea in lineas:
        code_bar = linea.strip()  
        try:
            code_bar = int(code_bar)
            print('----------------')
            print(f'code_bar : {code_bar}')
            # Si crea el code_bar a int, esta bueno y se pide el producto a la API
            # Si no se puede convertir a int es porq esta vacio o leyo mal 
            dict_of_product = get_product_from_api(code_bar)
            print(dict_of_product)
            create_product_from_dict(dict_of_product)
            print('---------------')
        except ValueError:
            print(f"{code_bar} no se puede convertir a entero.")
    # con los codigos pregunto a la API (OpenFoodFacts)
    # crear un producto con los valores devueltos

    pass

# Clase para subir una imagen al servidor mediante API REST
class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si la respiesta es valida se muestra la respuesta como json: "image": "/media/media/only_code.jpg"
            # print(f'serializeer.data: {serializer.data}')
            # path_image = serializer.data.get('image')
            # hay que tener cuidado porq la imagen no esta dentro de esta carpeta

            ruta_archivo = serializer.data.get('image')
            partes = ruta_archivo.rsplit('/', 1)
            nombre_archivo = partes[-1]
            path = settings.MEDIA_ROOT + '\\media\\'
            path = path.replace('\\', '/') + nombre_archivo
            func_to_get_values(path_image=path) # se hace que se evalue la imagen 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



   
