from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Player

from .serializers import PlayerSerializer
from rest_framework.response import Response
from rest_framework import generics



class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple viewset for listing players
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    
    
class PlayerNameList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def list(self, request, *args, **kwargs):
        """
        A simple list view for listing all player names
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response([item['Name'] for item in serializer.data])
    
class PlayerByName(generics.ListAPIView):
    serializer_class = PlayerSerializer
    
    def get_queryset(self):
        """
        A simple view for retrieving players by name
        """
        playerName = self.kwargs['name']
        return Player.objects.filter(Name=playerName)
    
class ClubList(generics.ListAPIView):
    serializer_class = PlayerSerializer
    
    def get_queryset(self):
            return Player.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Group players by club
        clubs_dict = {}
        for player_data in serializer.data:
            club_name = player_data['Club']
            player_name = player_data['Name']

            if club_name not in clubs_dict:
                clubs_dict[club_name] = {'name': club_name, 'players': []}

            clubs_dict[club_name]['players'].append(player_name)

        clubs_list = [club_info for club_info in clubs_dict.values()]
        return Response(clubs_list)
    
class AttributeNameList(generics.ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def list(self, request, *args, **kwargs):
        """
        A simple list view for listing all player names
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response([item['Attribute'] for item in serializer.data])