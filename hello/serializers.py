from rest_framework import serializers
from .models import *

class ChampSerializer(serializers.ModelSerializer):
    class Meta:
        model = champ
        fields = '__all__'

class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = lane
        fields = '__all__'