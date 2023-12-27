from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Player

from .serializers import PlayerSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed
    """
    queryset = Player.objects.all()
    serializer_class= PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]