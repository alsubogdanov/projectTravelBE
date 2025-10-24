from rest_framework import generics, permissions
from ..models import SocialLink
from ..serializers import SocialLinkSerializer


class SocialLinkListView(generics.ListAPIView):
    """
    Публичное API: возвращает список всех соцсетей.
    Доступно без авторизации.
    """
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.AllowAny]