from rest_framework import serializers
from bearer_auth.models import AccessToken

class AccessTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessToken
        fields = '__all__'