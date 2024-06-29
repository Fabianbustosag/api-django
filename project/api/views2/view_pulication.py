from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import viewsets
from ..serializers import PublicationSerializer
from ..models import Publication

class PublicationModelView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer