Django rest Bearer Auth
---

Must have installed `rest_framework`, then install `bearer-auth` via pip and add it to `settings.py`

```python
pip install django-rest-auth-bearer
```

```python
INSTALLED_APPS: [
  ...,
  'rest_framework',
  'bearer_auth',
]
```

Add custom authentication to `BearerTokenAuth`

```python
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'bearer_auth.authentication.BearerTokenAuth',
    ),
```

Add `TOKEN_EXPIRES_IN` timespan to `settings.py`

```python
TOKEN_EXPIRES_IN = 2  #2hours
```

Customize `urls.py`

```python
from bearer_auth.views import ObtainToken

...
path('auth/token', ObtainToken.as_view()),
```

From frontend side, send request as following for acquire token

```json
"username": "username",
"password": "password123",
"grant_type": "password"  //must be password
```
As for response:
```json
{
  "token_type":"Bearer",
  "access_token":"c2fbea30732f113bbf879e51b2e49544d2de2d10"
  "refresh_token":"8ab39baa8f29041a891767a9323500073c9ee8e89e944af759",
  "expires_in":1
}
```

Moreover to refresh current token, send `refresh_token` value with grant_type `refresh_token` to same endpoint

```json
{
  "refresh_token":"8ab39baa8f29041a891767a9323500073c9ee8e89e944af759",
  "grant_type": "refresh_token"
}
```
