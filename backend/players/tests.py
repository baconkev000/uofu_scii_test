from api.users.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class PlayerTestCase(APITestCase):
    """Tests related to the Player model."""

    fixtures = ["soccer_small.json"]

    def setUp(self):
        """Set up required items for the tests."""
        self.client = APIClient()
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
        self.token = Token.objects.create(user=self.user)

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
        self.client.force_login(user=self.user)
        player_list_response = self.client.get(
            "/api/players/",
            format="json",
        )
        self.assertEqual(player_list_response.status_code, status.HTTP_200_OK)

    def test_cannot_get_player_list_without_token(self):
        """Cannnot get list of all players without an auth token"""
        player_list_response = self.client.get(
            "/api/players/",
            format="json",
        )
        self.assertEqual(player_list_response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_player_by_name(self):
        """Can get a player by name"""
        self.client.force_login(user=self.user)
        player_list_response = self.client.get(
            "/api/players/Cristiano%20Ronaldo/",
            format="json",
        )
        self.assertEqual(player_list_response.status_code, status.HTTP_200_OK)

    def test_get_clubs_list(self):
        """Can get list of all clubs"""
        self.client.force_login(user=self.user)
        clubs_list_response = self.client.get(
            "/api/clubs/",
            format="json",
        )
        self.assertEqual(clubs_list_response.status_code, status.HTTP_200_OK)

    def test_get_attributes_list(self):
        """Can get list of all attribute names"""
        self.client.force_login(user=self.user)
        attributes_list_response = self.client.get(
            "/api/attributes/",
            format="json",
        )
        self.assertEqual(attributes_list_response.status_code, status.HTTP_200_OK)
