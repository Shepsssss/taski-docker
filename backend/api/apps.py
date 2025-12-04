"""Модуль администрирования для приложения API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Docstring for ApiConfig."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
