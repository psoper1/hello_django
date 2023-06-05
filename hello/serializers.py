from rest_framework import serializers
from .models import *


class LaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = lane
        fields = '__all__'

class ChampSerializer(serializers.ModelSerializer):
    lane = LaneSerializer(many=True)
    class Meta:
        model = champ
        fields = '__all__'