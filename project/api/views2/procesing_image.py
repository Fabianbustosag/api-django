import re
import cv2
import requests
import json
from pytesseract import *

pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# extraigo el texto de la imagen
def get_text_from_image(image_path: str) -> str: 
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold_img)
    return text

def get_bar_codes(text: str):
    lineas = text.splitlines()
    for linea in lineas:
        code_bar = linea.strip()  
        try:
            code_bar = int(code_bar)
        except ValueError:
            print(f"{code_bar} no se puede convertir a entero.")
    pass

# esta funcion debe retornan un diccionario con los datos requeridos para hacer un nuevo prodcuto
def get_product_from_api(bar_code: int):
    url = f'https://world.openfoodfacts.org/api/v3/product/{bar_code}.json'

    fallback_img_src = 'http://127.0.0.1:8000/media/media/food_generic_2.png'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.content)
        food_name = data['product']['brands'] # Name Product
        category = data['product']['categories'] # categories, pueden ser muchos
        food_amount_g = data['product']['quantity']
        print('food amount',food_amount_g)
        # img_src = data['product']['image_url']
        img_src = data.get('image_url', fallback_img_src) 
        print('image src',img_src)

        img_response = requests.head(img_src)
        if img_response.status_code != 200:
            img_src = fallback_img_src

        return {
            'food_name': food_name,
            'category': category,
            'food_amount_g': food_amount_g,
            'img_src': img_src
        }
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except Exception as err:
        return f"An error occurred: {err}"
    
def limpiar_y_convertir(cadena):
    # Usar una expresión regular para eliminar cualquier cosa que no sea un número o un punto decimal
    cadena_limpia = re.sub(r'[^\d.]+', '', cadena)
    # Convertir la cadena resultante a float
    try:
        valor_float = float(cadena_limpia)
        return valor_float
    except ValueError:
        return f"Error: no se pudo convertir '{cadena}' a float."

# Data from API, OpenFoodFacts (there re more)
# - nombre: x.product.brands
# - tags: x.product.brands_tags[0], x.product.brands_tags[1] (is a list) (lenght is not fixed )
# - categoria: x.product.categories
# - alergias: x.product.allergens_from_user
# - cantidad en gramos: x.product.quantity
# - image: x.product.image_url