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

# C:\Users\fabian\Documents\api-django\project\media
# C:\Users\fabian\Documents\api-django\project\api\views2
# ../../media/media/only_code.jpg
# Clase para subir una imagen al servidor mediante API REST
class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        # print(request.data)
        if serializer.is_valid():
            serializer.save()
            # Si la respiesta es valida se muestra la respuesta como json: "image": "/media/media/only_code.jpg"
            # print(f'serializeer.data: {serializer.data}')
            # path_image = serializer.data.get('image')
            # hay que tener cuidado porq la imagen no esta dentro de esta carpeta
            path_image = r'C:\\Users\\fabian\\Documents\\api-django\\project\\media\\media\\boleta_2_code.jpg' # ruta donde quedo almacenada la imagen

            ruta_archivo = serializer.data.get('image')
            partes = ruta_archivo.rsplit('/', 1)
            nombre_archivo = partes[-1]
            path = settings.MEDIA_ROOT + '\\media\\'
            path = path.replace('\\', '/') + nombre_archivo
            func_to_get_values(path_image=path) # se hace que se evalue la imagen / serializer.data 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def test_eval2(request):
    path_image = r'C:\\Users\\fabian\\Documents\\api-django\\project\\media\\media\\boleta_2_code.jpg' # ruta donde quedo almacenada la imagen
    path_image = r'../media/media/boleta_2_code.jpg'
    path = settings.MEDIA_ROOT + '\\media\\'
    path = path.replace('\\', '/')
    # print(f"path_image: {path_image}")
    # func_to_get_values(path_image=path_image) # se hace que se evalue la imagen / serializer.data 
    # return HttpResponse(settings.MEDIA_ROOT)
    return HttpResponse(path) 

def test_eval(request):
    path_image = r'C:\\Users\\fabian\\Documents\\api-django\\project\\media\\media\\boleta_2_code.jpg' # ruta donde quedo almacenada la imagen
    path_image = r'../media/media/boleta_2_code.jpg'
    path = settings.MEDIA_ROOT
    # print(f"path_image: {path_image}")
    func_to_get_values(path_image=path_image) # se hace que se evalue la imagen / serializer.data 
    # return HttpResponse(settings.MEDIA_ROOT)
    return HttpResponse(path)
   

# ruta_archivo = '/media/media/only_code.jpg'

# # Usando el método rsplit() para dividir la cadena por '/'
# partes = ruta_archivo.rsplit('/', 1)

# # partes contendrá ['', 'only_code.jpg']
# # El último elemento de partes es lo que está después de la última barra
# nombre_archivo = partes[-1]


# La diferencia con el otro es que se le debe pasar por parametro el valor de la llave primaria de User_data
# def create_product_from_dict2(product_data: dict, pk: int):
#     user = UserData.objects.get(pk=pk)
#     try:
#         print('create_product')
#         print('product: ', product_data)
#         product = Food.objects.create(
#             user = user,
#             food_name = product_data['food_name'], # str
#             # category = product_data['category'], # str
#             food_amount_g = limpiar_y_convertir(product_data['food_amount_g']), # Float
#             img_src = product_data['img_src'] # str
#         )
#         return product
#     except Exception as e:
#         return f"An error occurred while saving to the database: {e}"
        
   
