"""Bearer auth urls"""
from django.urls import path
from bearer_auth.views import ObtainAuthToken, AccessTokenViewSet

app_name = 'bearer_auth'

urlpatterns = [
    path("list/", AccessTokenViewSet.as_view({'get': 'list'}), name="tokens")
]
