from rest_framework import serializers
from .models import Player
from datetime import datetime

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'