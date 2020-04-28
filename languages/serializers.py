from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.HyperlinkedModelSerializer):  #Hyperlinked is used to show the url of respective object
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')