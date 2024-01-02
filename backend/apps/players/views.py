from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework import generics

from .models import Player

from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A Simple Viewset for listing players and retreiving a player by name
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    # add SessionAuthentication & BasicAuthentication for auth token requirement
    authentication_classes = []
    # add permissions.IsAuthenticate for auth token requirement
    permission_classes = []
    lookup_field = "Name"


class ClubListView(generics.ListAPIView):
    """
    A simple list view for listing clubs and the associated players
    """

    serializer_class = PlayerSerializer

    def get_queryset(self):
        return Player.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # Group players by club
        clubs_dict = {}
        i = 0
        for player_data in serializer.data:
            club_name = player_data["Club"]
            player_name = player_data["Name"]

            if club_name not in clubs_dict:
                i += 1
                clubs_dict[club_name] = {"id": i, "name": club_name, "players": []}

            clubs_dict[club_name]["players"].append(player_name)

        clubs_list = [club_info for club_info in clubs_dict.values()]
        return Response(clubs_list)


class PlayerAttributesListView(generics.ListAPIView):
    """
    A simple list view for listing player attribute names
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset.first())  # Get the first player's data

        # Exclude specific fields from attribute names
        excluded_fields = ["id", "Name"]
        attribute_names = [key for key in serializer.data.keys() if key not in excluded_fields]

        return Response(attribute_names)
