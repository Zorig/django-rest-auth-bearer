from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

from rest_framework.viewsets import ModelViewSet
from bearer_auth.serializers import AccessTokenSerializer

from bearer_auth.models import AccessToken
from bearer_auth.settings import token_settings


class ObtainToken(ObtainAuthToken):
    model = AccessToken
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            if request.data['grant_type'] == 'password':
                token = AccessToken.objects.create(user=user)
                return Response({
                    "token_type": "Bearer",
                    "access_token": token.key,
                    "refresh_token": token.refresh_token,
                    "expires_in": token_settings.TOKEN_EXPIRES_IN
                })
            elif request.data['grant_type'] == 'refresh_token':
                try:
                    token = AccessToken.objects.get(
                        refresh_token=request.data['refresh_token'],
                        active=True)
                except AccessToken.DoesNotExist:
                    token = None
                if token is not None:
                    token.delete()
                    new_token = AccessToken.objects.create(user=user)
                    return Response({
                        "token_type": "Bearer",
                        "access_token": new_token.key,
                        "refresh_token": new_token.refresh_token,
                        "expires_in": token_settings.TOKEN_EXPIRES_IN
                    })
                else:
                    return Response(
                        serializer.errors, status=HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class AccessTokenViewSet(ModelViewSet):
    queryset = AccessToken.objects.all()
    serializer_class = AccessTokenSerializer