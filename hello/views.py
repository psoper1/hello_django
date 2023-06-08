from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework import viewsets, generics
from .models import champ, lane
from .serializers import ChampSerializer, LaneSerializer
from django.http import JsonResponse

def home(request):
    return HttpResponse("Hello, Django!")

class ChampDetailAPIView(generics.RetrieveAPIView):
    queryset = champ.objects.all()
    serializer_class = ChampSerializer

class ChampListCreateView(generics.ListCreateAPIView):
    queryset = champ.objects.all()
    serializer_class = ChampSerializer

class LaneListCreateView(generics.ListCreateAPIView):
    queryset = lane.objects.all()
    serializer_class = LaneSerializer

class LaneDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = lane.objects.all()
    serializer_class = LaneSerializer

def get_riot_api_key(request):
    api_key = settings.RIOT_API_KEY
    return JsonResponse({'api_key': api_key})