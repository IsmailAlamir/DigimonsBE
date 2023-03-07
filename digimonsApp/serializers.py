from rest_framework import serializers
from .models import Digimon
class DigimonsSerializer(serializers.ModelSerializer):
        class Meta:
            model= Digimon
            fields='__all__'
