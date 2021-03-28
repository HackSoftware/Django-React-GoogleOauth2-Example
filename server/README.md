# Local Development

0. The project uses sqlite3 for local development so you don't need any DB configuration :v:
1. Create a new virtual env. We use the latest stable version of Python for this project -> `3.9`
1. Install the requirements -> `pip install -r requirements.txt`
1. Run the migrations -> `python3 manage.py migrate`
1. Generate Google Client ID and Secret -> you can follow [this article](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid) from Google
1. Add your Client ID and Secret to the `.env` file:

```
DJANGO_GOOGLE_OAUTH2_CLIENT_ID=<your-client-id-here>
DJANGO_GOOGLE_OAUTH2_CLIENT_SECRET=<your-client-secret-here>
```

6. We're ready! Run the server -> `python3 manage.py runserver`
7. _(Optional)_ If you want to create a new superuser in order to use the Django admin, you can do the following:

- Run `python3 manage.py shell_plus`
- Execute the following code:

```
from users.services import user_create_superuser

user_create_superuser(
    email='your_email@here.com',
    password='password-that-you-are-going-to-use-to-access-the-admin'
)
```

- You now have a new superuser! You cann navigate to `http://localhost:8000/admin/` in order to use the Django admin.
