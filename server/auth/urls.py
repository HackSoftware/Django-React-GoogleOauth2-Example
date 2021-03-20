from django.urls import path, include

from auth.apis import LoginApi

login_patterns = [
    path('', LoginApi.as_view(), name='login'),
]

urlpatterns = [
    path('login/', include(login_patterns)),
    # path('logout/', UserLogoutApi.as_view(), name='logout'),
]
