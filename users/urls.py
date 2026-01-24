from django.contrib.auth import views as auth_views
from django.urls import include, path

from .views import (
    CustomPasswordChangeDoneView,
    CustomPasswordChangeView,
    CustomPasswordResetConfirmView,
    CustomPasswordResetView,
    SignupView,
)

urlpatterns = [
    path(
        "password_reset/",
        CustomPasswordResetView.as_view(
            html_email_template_name="registration/password_reset_html_email.html"
        ),
        name="password_reset",
    ),
    path(
        "reset/<uidb64>/<token>/",
        CustomPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "password_change/",
        CustomPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password_change/done/",
        CustomPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    path("signup/", SignupView.as_view(), name="signup"),
    path("", include("django.contrib.auth.urls")),
]
app_name = "users"
