import re
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


from .models import Food, UserData

def clean(cadena):
    # Usar una expresión regular para eliminar cualquier cosa que no sea un número o un punto decimal
    cadena_limpia = re.sub(r'[^\d.]+', '', cadena)
    # Convertir la cadena resultante a float
    try:
        valor_float = float(cadena_limpia)
        return valor_float
    except ValueError:
        return f"Error: no se pudo convertir '{cadena}' a float."

# Create your views here.
def hello(request):
    return HttpResponse("hello world")
    # return HttpResponse(settings.MEDIA_ROOT)




# view para model food
def create_model(request):
    user = UserData.objects.get(pk=1)

    product_data = {
        'food_name': 'bon o bon,Arcor', 
        'category': 'Botanas,Snacks dulces,Galletas y pasteles,Galletas,Galletas rellenas', 
        'food_amount_g': '95 g', 
        'img_src': 'https://images.openfoodfacts.org/images/products/780/222/564/0770/front_es.9.400.jpg'
        }

    Food.objects.create(
            user = user,
            food_name = product_data['food_name'], # str
            # category = product_data['category'], # str
            food_amount_g = clean(product_data['food_amount_g']), # Float
            img_src = product_data['img_src'] # str
        )
    return HttpResponse("Product")

