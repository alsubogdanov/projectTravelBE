from rest_framework import generics, status, permissions
from .models import Article
from .serializers import ArticleSerializer

# Список статей + добавление
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
   #  permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

# Одна статья (просмотр / обновление / удаление)
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer