from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe
from rest_framework import permissions

# Create your views here.

class RecipeList(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

