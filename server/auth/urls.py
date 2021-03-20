from django.urls import path, include

from auth.apis import LoginApi, LogoutApi

login_patterns = [
    path('', LoginApi.as_view(), name='login'),
]

urlpatterns = [
    path('login/', include(login_patterns)),
    path('logout/', LogoutApi.as_view(), name='logout'),
]
