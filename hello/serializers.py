from rest_framework import serializers
from .models import *

class ChampSerializer(serializers.ModelSerializer):
    class Meta:
        model = champ
        fields = '__all__'