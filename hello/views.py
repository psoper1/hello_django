from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics
from .models import champ
from .serializers import ChampSerializer

def home(request):
    return HttpResponse("Hello, Django!")

class ChampDetailAPIView(generics.RetrieveAPIView):
    queryset = champ.objects.all()
    serializer_class = ChampSerializer

class ChampListCreateView(generics.ListCreateAPIView):
    queryset = champ.objects.all()
    serializer_class = ChampSerializer