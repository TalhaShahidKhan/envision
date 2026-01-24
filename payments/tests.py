import hashlib
import hmac
import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Credit, Payment

User = get_user_model()


class PaymentTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="payuser",
            password="password123",
            email="pay@example.com",
            upscale_credit=0,
        )
        self.credit = Credit.objects.create(number_of_credits=10, price=5)
        self.webhook_url = reverse("pay:webhook")

    def test_webhook_invalid_signature(self):
        """Test that webhook fails with invalid signature."""
        response = self.client.post(
            self.webhook_url,
            data=json.dumps({"event_type": "transaction.completed"}),
            content_type="application/json",
            HTTP_PADDLE_SIGNATURE="invalid_signature",
        )
        self.assertEqual(response.status_code, 401)
        self.assertIn("Invalid webhook signature", response.json()["message"])

    def test_webhook_transaction_completed(self):
        """Test successful credit addition via webhook (mocking verification)."""
        # Note: Since we can't easily generate a valid Paddle signature without their SDK internals,
        # and the Verifier uses request.body, we'll patch the Verifier or just test the logic.
        # For this test, let's assume we patch the verifier to always return True.

        payload = {
            "event_type": "transaction.completed",
            "data": {
                "custom_data": {
                    "credit_id": str(self.credit.id),
                    "user_email": self.user.email,
                }
            },
        }

        with patch(
            "paddle_billing.Notifications.Verifier.Verifier.verify", return_value=True
        ):
            response = self.client.post(
                self.webhook_url,
                data=json.dumps(payload),
                content_type="application/json",
                HTTP_PADDLE_SIGNATURE="mocked",
            )

        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.upscale_credit, 10)
        self.assertTrue(
            Payment.objects.filter(user=self.user, credit=self.credit).exists()
        )


from unittest.mock import patch
