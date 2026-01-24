from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Image

User = get_user_model()


class CloudinaryViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser",
            password="password123",
            email="test@example.com",
            upscale_credit=10,
        )
        self.image = Image.objects.create(
            user=self.user,
            public_id="test_public_id",
            image_name="test_image.jpg",
            upload_link="https://res.cloudinary.com/test/image/upload/test_public_id.jpg",
        )
        self.upload_url = reverse("cloudinary:upload")
        self.client.login(username="testuser", password="password123")

    def test_upload_view_requires_login(self):
        """Test that the upload view redirects to login for anonymous users."""
        self.client.logout()
        response = self.client.post(self.upload_url)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/users/login/"))

    def test_upload_view_no_image(self):
        """Test that the upload view shows error when no image is provided."""
        response = self.client.post(self.upload_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No image provided")

    def test_upscale_task(self):
        """Test the upscale AI task."""
        url = reverse(
            "cloudinary:task",
            kwargs={"public_id": self.image.public_id, "task": "upscale"},
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "e_upscale")
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 9)

    def test_background_removal_task(self):
        """Test the background removal AI task."""
        url = reverse(
            "cloudinary:task",
            kwargs={"public_id": self.image.public_id, "task": "bg_remove"},
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "e_background_removal")
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 9)

    def test_generative_fill_task(self):
        """Test the generative fill AI task."""
        url = reverse(
            "cloudinary:task",
            kwargs={"public_id": self.image.public_id, "task": "gen_fill"},
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "b_gen_fill")
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 9)

    def test_extract_object_task(self):
        """Test the extract object AI task."""
        url = reverse(
            "cloudinary:task", kwargs={"public_id": self.image.public_id, "task": "ext"}
        )
        response = self.client.post(url, {"ext": "cat"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "e_extract:prompt_(cat)")
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 9)

    def test_generative_replace_task(self):
        """Test the generative replace AI task."""
        url = reverse(
            "cloudinary:task",
            kwargs={"public_id": self.image.public_id, "task": "gen_replace"},
        )
        response = self.client.post(url, {"from": "dog", "to": "lion"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "e_gen_replace:from_dog;to_lion")
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 9)

    def test_insufficient_credits(self):
        """Test that tasks fail when user has no credits."""
        self.user.upscale_credit = 0
        self.user.save()
        url = reverse(
            "cloudinary:task",
            kwargs={"public_id": self.image.public_id, "task": "upscale"},
        )
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Insufficient credits")
