from users.models import User


def user_get_me(*, user: User):
    return {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'me': user_get_me(user=user),
    }
