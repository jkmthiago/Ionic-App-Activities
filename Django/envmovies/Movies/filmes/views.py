from django.shortcuts import render
from filmes.serializers import AtorSerializer, MovieSerializer
from filmes.models import Ator, Movie
from rest_framework import viewsets
from rest_framework.authtoken.admin import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
class ActorViewSet (viewsets.ModelViewSet):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)