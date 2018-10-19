"""Bearer auth authentication"""
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from bearer_auth.models import AccessToken


class BearerTokenAuth(TokenAuthentication):
    """Bearer token authentication"""
    model = AccessToken
    keyword = 'Bearer'

    def authenticate_credentials(self, key):
        try:
            token = self.model.objects.get(key=key)
        except self.model.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid Token')

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User is not active")

        if token.expired():
            raise exceptions.AuthenticationFailed("Expired")
        return (token.user, token)
