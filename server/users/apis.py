from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class UserGoogleOAuth2CallbackApi(APIView):
    class InputSerializer(serializers.Serializer):
        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)

    def get(self, request):
        return Response()


class UserGetApi(APIView):
    class OutputSerializer(serializers.Serializer):
        email = serializers.CharField()
        name = serializers.CharField()

    def get(self, request):
        user = request.user

        serializer = self.OutputSerializer(user)

        return Response(serializer.data)


class UserLogoutApi(APIView):
    def post(self, request):
        # TODO: Remove JWT
        return Response()
