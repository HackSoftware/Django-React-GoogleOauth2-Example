import requests
from typing import Optional, Dict, Any

from django.conf import settings
from django.core.exceptions import ValidationError

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler, jwt_encode_handler

from utils import get_now
from users.models import User
from users.services import user_record_login


GOOGLE_TOKEN_OBTAIN_URL = 'https://oauth2.googleapis.com/token'
GOOGLE_TOKEN_INFO_URL = 'https://www.googleapis.com/oauth2/v3/tokeninfo'
GOOGLE_USER_INFO_URL = 'https://www.googleapis.com/oauth2/v3/userinfo'


def jwt_login(user: User) -> Optional[dict]:
    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)

    if api_settings.JWT_AUTH_COOKIE:
        expiration = get_now().utcnow() + api_settings.JWT_EXPIRATION_DELTA

        is_production_env = settings.PRODUCTION_SETTINGS

        cookie_data = {
            'key': api_settings.JWT_AUTH_COOKIE,
            'value': token,
            'expires': expiration,
            'httponly': True,
            'secure': is_production_env
        }

        if is_production_env:
            cookie_data['samesite'] = None

        user_record_login(user=user)

        return cookie_data


def google_get_access_token(*, code: str, redirect_uri: str) -> str:
    data = {
        'code': code,
        'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
        'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }

    response = requests.post(GOOGLE_TOKEN_OBTAIN_URL, data=data)

    if not response.ok:
        raise ValidationError('Failed to obtain access token from Google')

    access_token = response.json()['access_token']

    return access_token


def google_validate_access_token(*, access_token: str) -> Optional[bool]:
    response = requests.get(
        GOOGLE_TOKEN_INFO_URL,
        params={'access_token': access_token}
    )

    if not response.ok:
        raise ValidationError('Access token is invalid')

    return True


def google_get_user_info(*, access_token: str) -> Dict[str, Any]:
    response = requests.get(
        GOOGLE_USER_INFO_URL,
        params={'access_token': access_token}
    )

    if not response.ok:
        raise ValidationError('Failed to obtain user info from Google.')

    return response.json()
