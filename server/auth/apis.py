from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.views import ObtainJSONWebToken

from django.urls import reverse
from django.conf import settings
from django.shortcuts import redirect

from api.mixins import ApiErrorsMixin, PublicApiMixin, ApiAuthMixin

from users.services import user_record_login, user_change_secret_key, user_get_or_create

from auth.services import jwt_login, google_get_access_token, google_get_user_info


class LoginApi(ApiErrorsMixin, ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        # For reference:
        # https://github.com/jpadilla/django-rest-framework-jwt/blob/master/rest_framework_jwt/views.py#L54
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.object.get('user') or request.user
        user_record_login(user=user)

        return super().post(request, *args, **kwargs)


class GoogleLoginApi(PublicApiMixin, ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)

    def get(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data

        code = validated_data.get('code')
        error = validated_data.get('error')

        if error or not code:
            # TODO: Encode error as query param
            return redirect(settings.BASE_FRONTEND_URL)

        domain = settings.BASE_BACKEND_URL
        api_uri = reverse('api:v1:auth:login-with-google')
        redirect_uri = f'{domain}{api_uri}'

        access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)

        user_data = google_get_user_info(access_token=access_token)

        profile_data = {
            'email': user_data['email'],
            'first_name': user_data.get('givenName', ''),
            'last_name': user_data.get('familyName', ''),
        }

        user, created = user_get_or_create(**profile_data)

        if created:
            # TODO: Do not login, just return to FE
            pass

        response = redirect(settings.BASE_FRONTEND_URL)
        jwt_cookie_data = jwt_login(user=user)

        response.set_cookie(**jwt_cookie_data)

        return response


class LogoutApi(ApiAuthMixin, ApiErrorsMixin, APIView):
    def post(self, request):
        """
        Logs out user by removing JWT cookie header.
        """
        user_change_secret_key(user=request.user)

        response = Response(status=status.HTTP_202_ACCEPTED)
        response.delete_cookie(settings.JWT_AUTH['JWT_AUTH_COOKIE'])

        return response
