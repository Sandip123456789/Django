from django.shortcuts import render
from .models import Language
from rest_framework import viewsets
from .serializers import LanguageSerializer;

# Create your views here.
class LanguageList(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer