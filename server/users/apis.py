from rest_framework.views import APIView
from rest_framework.response import Response

from api.mixins import ApiErrorsMixin, ApiAuthMixin

from users.selectors import user_get_me


class UserMeApi(ApiAuthMixin, ApiErrorsMixin, APIView):
    def get(self, request, *args, **kwargs):
        return Response(user_get_me(user=request.user))
