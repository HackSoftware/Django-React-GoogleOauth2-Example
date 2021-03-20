from rest_framework_jwt.views import ObtainJSONWebToken

from api.mixins import ApiErrorsMixin

from users.services import user_record_login


class LoginApi(ApiErrorsMixin, ObtainJSONWebToken):
    def post(self, request, *args, **kwargs):
        # For reference:
        # https://github.com/jpadilla/django-rest-framework-jwt/blob/master/rest_framework_jwt/views.py#L54
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.object.get('user') or request.user
        user_record_login(user=user)

        return super().post(request, *args, **kwargs)


# class LogoutApi(ApiAuthMixin, ApiErrorsMixin, APIView):
#     def post(self, request):
#         """
#         Logs out user by removing JWT cookie header.
#         """
#         user_rotate_token(user=request.user)

#         response = Response(status=status.HTTP_202_ACCEPTED)
#         response.delete_cookie(settings.JWT_AUTH['JWT_AUTH_COOKIE'])

#         return response
