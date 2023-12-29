from .models import Player
from api.users.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from rest_framework.test import APITestCase
#from rest_framework_simplejwt.tokens import RefreshToken


class PlayerTestCase(APITestCase):
    """Tests related to the Player model."""

    fixtures = ["soccer_small.json"]

    def setUp(self):
        """Set up required items for the tests."""
        super().setUp()

        self.user = User.objects.create_user(
            username="test",
            email="test@test.com",
            password="password",
        )

        self.superuser = User.objects.create_superuser(
            username="test_super",
            email="super@test.com",
            password="password",
        )

    def tearDown(self):
        """Delete things in the reverse of the order they were made"""
        self.superuser.delete()
        self.user.delete()

    def test_create_user(self):
        """Our user in setup is a user"""
        self.assertIsInstance(self.user, User)
        self.assertFalse(self.user.is_superuser)

    def test_get_player_list(self):
        """Can get list of all players"""
        player_list_response = self.client.get(
            "/api/players/",
            format="json",
        )
        self.assertEqual(player_list_response.status_code, status.HTTP_200_OK)
    
    # def test_get_player_by_name(self):
    #     """Can get a player by name"""
    #     player_list_response = self.client.get(
    #         "/api/players/Cristiano%20Ronaldo/",
    #         format="json",
    #     )
    #     self.assertEqual(player_list_response.status_code, status.HTTP_200_OK)

    # def test_get_clubs_list(self):
    #     """Can get list of all players"""
    #     clubs_list_response = self.client.get(
    #         "/api/clubs/",
    #         format="json",
    #     )
    #     self.assertEqual(clubs_list_response.status_code, status.HTTP_200_OK)

    # def test_get_attributes_list(self):
    #     """Can get list of all players"""
    #     attributes_list_response = self.client.get(
    #         "/api/attributes/",
    #         format="json",
    #     )
    #     self.assertEqual(attributes_list_response.status_code, status.HTTP_200_OK)