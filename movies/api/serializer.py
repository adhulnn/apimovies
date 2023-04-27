from rest_framework import serializers
from .models import*

class MovieSerializer(serializers.Serializer):
    name=serializers.CharField()
    year=serializers.IntegerField()
    director=serializers.CharField()
    genre=serializers.CharField()
   
