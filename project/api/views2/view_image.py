from django.shortcuts import render
from django.http import HttpResponse
from ..forms import MyModelForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import ImageUploadSerializer

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


# Clase para subir una imagen al servidor mediante API REST
class ImageUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)