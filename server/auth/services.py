from typing import Optional

from django.conf import settings

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from utils import get_now
from users.models import User
from users.services import user_record_login


def jwt_login(user: User) -> Optional[dict]:
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    if api_settings.JWT_AUTH_COOKIE:
        expiration = get_now().utcnow() + api_settings.JWT_EXPIRATION_DELTA

        cookie_data = {
            'key': api_settings.JWT_AUTH_COOKIE,
            'value': token,
            'expires': expiration,
            'httponly': True,
            'secure': settings.PRODUCTION_SETTINGS
        }

        user_record_login(user=user)

        return cookie_data
