from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView, CommentListCreateView

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path('articles/<int:article_id>/comments/', CommentListCreateView.as_view(), name='comments'),

]