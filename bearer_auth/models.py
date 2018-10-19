"""Bearer Token Model"""
import os
import binascii
import datetime
from django.db import models
from django.utils import timezone
from django.conf import settings
from bearer_auth.settings import token_settings


class AccessToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    refresh_token = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key(20)
            self.refresh_token = self.generate_key(25)
        return super(AccessToken, self).save(*args, **kwargs)

    def generate_key(self, length):
        """Generate random key"""
        return binascii.hexlify(os.urandom(length)).decode()

    def expired(self):
        """Check expire"""
        if settings.USE_TZ is True:
            now = timezone.now()
        else:
            now = datetime.datetime.now()
        if self.created_at < now - datetime.timedelta(hours=token_settings.TOKEN_EXPIRES_IN):
            return True
        return False
