#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Warning for missing production environment variables
    if os.environ.get("DJANGO_SETTINGS_MODULE") == "core.settings":
        from django.conf import settings

        critical_vars = [
            "CLOUDINARY_CLOUD_NAME",
            "CLOUDINARY_API_KEY",
            "CLOUDINARY_API_SECRET",
            "DATABASE_URL",
            "PADDLE_API_SECRET_KEY",
        ]
        if not settings.DEBUG:
            for var in critical_vars:
                if not os.environ.get(var):
                    print(f"⚠️  WARNING: {var} is not set in environment variables!")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
