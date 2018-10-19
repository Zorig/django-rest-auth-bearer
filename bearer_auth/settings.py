"""
Provide access to settings
"""
from datetime import timedelta
from django.conf import settings


class TokenSettings(object):

    @property
    def TOKEN_EXPIRES_IN(self):
        """
        Return allowed lifespan of token
        """
        try:
            val = settings.TOKEN_EXPIRES_IN
        except AttributeError:
            val = timedelta(hours=2)

        return val


token_settings = TokenSettings()
