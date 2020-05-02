from django.shortcuts import render
from .models import Language, Paradigm, Programmer
from rest_framework import viewsets, permissions
from .serializers import LanguageSerializer, ParadigmSerializer, ProgrammerSerializer

# Create your views here.
class LanguageList(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ParadigmList(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerList(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer