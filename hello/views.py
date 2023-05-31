from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import champ
from .serializers import ChampSerializer

def home(request):
    return HttpResponse("Hello, Django!")

class ChampViewSet(viewsets.ModelViewSet):
    queryset = champ.objects.all()
    serializer_class = ChampSerializer