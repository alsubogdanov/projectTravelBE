from rest_framework import generics, permissions
from ..models import AboutSection
from ..serializers import AboutSectionSerializer


class AboutSectionAdminView(generics.RetrieveUpdateAPIView):
    """
    Админский эндпоинт: позволяет получить (GET) и обновить (PUT/PATCH) раздел.
    Доступ: только администраторам (is_staff).
    """
    permission_classes = [permissions.IsAdminUser]  # проверяет request.user.is_staff
    serializer_class = AboutSectionSerializer
    queryset = AboutSection.objects.all()

    def get_object(self):
        return AboutSection.objects.first()