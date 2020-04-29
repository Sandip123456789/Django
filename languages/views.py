from django.shortcuts import render
from .models import Language, Paradigm, Programmer
from rest_framework import viewsets
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# Create your views here.
class LanguageList(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class ParadigmList(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerList(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer