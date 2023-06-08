from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from rest_framework import viewsets, generics
from .models import champ, lane
from .serializers import ChampSerializer, LaneSerializer
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

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

@cache_page(60 * 60)  # Cache the response for 1 hour
def get_riot_api_key(request):
    api_key = cache.get('riot_api_key')
    if api_key is None:
        api_key = settings.RIOT_API_KEY
        cache.set('riot_api_key', api_key)
    return JsonResponse({'api_key': api_key})