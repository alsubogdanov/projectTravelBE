from rest_framework import generics, permissions
from ..models import SocialLink,ContactMessage,AboutSection, ContactSection, Video
from ..serializers import SocialLinkSerializer, AboutSectionSerializer, ContactSectionSerializer,VideoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

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
     


class ContactSectionPublicView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ContactSectionSerializer
    queryset = ContactSection.objects.all()

    def get_object(self):
        return ContactSection.objects.first()
     
     
class VideoListPublicView(generics.ListAPIView):
    """
    Публичный API для получения списка всех видео
    """
    queryset = Video.objects.all()  # выбираем все видео
    serializer_class = VideoSerializer

@api_view(['POST'])
def contact_view(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if not all([name, email, message]):
        return Response({'error': 'Заполните все поля'}, status=400)
	
 	

    
    ContactMessage.objects.create(name=name, email=email, message=message)
    # Отправляем письмо
    send_mail(
        subject=f"Сообщение с сайта от {name}",
        message=f"Email: {email}\n\nСообщение:\n{message}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=['yourprojectmail@example.com'],
    )

    return Response({'success': True})