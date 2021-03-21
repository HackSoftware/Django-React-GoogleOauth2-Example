from django.urls import path

from users.apis import UserMeApi, UserInitApi


urlpatterns = [
    path('me/', UserMeApi.as_view(), name='me'),
    path('init/', UserInitApi.as_view(), name='init'),
]
