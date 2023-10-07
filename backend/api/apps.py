"""settings apps."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """class settings apps."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
