from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from django.conf import settings

from api.mixins import ApiErrorsMixin, ApiAuthMixin

from users.services import user_record_login, user_change_secret_key


class LoginApi(ApiErrorsMixin, ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        # For reference:
        # https://github.com/jpadilla/django-rest-framework-jwt/blob/master/rest_framework_jwt/views.py#L54
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.object.get('user') or request.user
        user_record_login(user=user)

        return super().post(request, *args, **kwargs)


class LogoutApi(ApiAuthMixin, ApiErrorsMixin, APIView):
    def post(self, request):
        """
        Logs out user by removing JWT cookie header.
        """
        user_change_secret_key(user=request.user)

        response = Response(status=status.HTTP_202_ACCEPTED)
        response.delete_cookie(settings.JWT_AUTH['JWT_AUTH_COOKIE'])

        return response
