from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status

from api.mixins import ApiErrorsMixin, ApiAuthMixin, PublicApiMixin

from auth.services import jwt_login

from users.services import user_get_or_create, user_record_login
from users.selectors import user_get_me


class UserMeApi(ApiAuthMixin, ApiErrorsMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response(user_get_me(user=request.user))


class UserInitApi(PublicApiMixin, ApiErrorsMixin, APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        first_name = serializers.CharField(required=False, default='')
        last_name = serializers.CharField(required=False, default='')

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user, created = user_get_or_create(**serializer.validated_data)

        if created:
            return Response(data={}, status=status.HTTP_201_CREATED)

        response = Response(data=user_get_me(user=user))
        jwt_cookie_data = jwt_login(user=user)

        response.set_cookie(**jwt_cookie_data)

        user_record_login(user=user)

        return response
