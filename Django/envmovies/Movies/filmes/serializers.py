from django.urls import path, include
from filmes.models import Ator, Movie
from rest_framework import routers, serializers, viewsets

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = ['nome', 'idade', 'created_date', 'gender']
        
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['nome', 'id_ator']