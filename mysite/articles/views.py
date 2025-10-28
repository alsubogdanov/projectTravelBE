from rest_framework import generics, status, permissions
from .models import Article
from .serializers import ArticleSerializer
from .models import Comment
from .serializers import CommentSerializer
# Список статей + добавление
class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
   #  permission_classes = [permissions.IsAuthenticated]
    serializer_class = ArticleSerializer

# Одна статья (просмотр / обновление / удаление)
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Comment.objects.filter(article_id=article_id, parent__isnull=True).order_by('-date')

    def perform_create(self, serializer):
        serializer.save()