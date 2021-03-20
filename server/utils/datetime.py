from datetime import datetime

from django.utils import timezone


def get_now() -> datetime:
    return timezone.now()
