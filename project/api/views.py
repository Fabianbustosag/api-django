from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def hello(request):
    return HttpResponse("hello world")
    # return HttpResponse(settings.MEDIA_ROOT)

# view para model food