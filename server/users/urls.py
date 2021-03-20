from django.urls import path

from users.apis import UserMeApi


urlpatterns = [
    path('me/', UserMeApi.as_view(), name='me'),
]
