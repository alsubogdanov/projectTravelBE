from rest_framework import generics, permissions
from ..models import SocialLink
from ..models import AboutSection
from ..serializers import SocialLinkSerializer, AboutSectionSerializer


class SocialLinkListView(generics.ListAPIView):
    """
    Публичное API: возвращает список всех соцсетей.
    Доступно без авторизации.
    """
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer
    permission_classes = [permissions.AllowAny]
    
    
class AboutSectionPublicView(generics.RetrieveAPIView):
   
    """
    Публичный GET для отображения раздела "О нас" на сайте.
    Доступ: AllowAny (все пользователи, включая неавторизованных).
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = AboutSectionSerializer
    queryset = AboutSection.objects.all()

    def get_object(self):
        # Берём первый (или None)
        return AboutSection.objects.first()