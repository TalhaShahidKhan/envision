from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Image

User = get_user_model()


class CloudinaryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="password123", email="test@example.com"
        )
        self.upload_url = reverse("cloudinary:upload")

    def test_upload_view_requires_login(self):
        """Test that the upload view redirects to login for anonymous users."""
        response = self.client.post(self.upload_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/users/login/"))

    def test_upload_view_authenticated(self):
        """Test that the upload view is accessible when logged in."""
        self.client.login(username="testuser", password="password123")
        # We don't provide an image, so it should return an error message, but not a redirect
        response = self.client.post(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No image provided")
