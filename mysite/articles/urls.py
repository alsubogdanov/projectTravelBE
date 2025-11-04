from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView, CommentListCreateView,PopularArticlesViewSet,LatestArticlesViewSet

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path('articles/<int:article_id>/comments/', CommentListCreateView.as_view(), name='comments'),
	 path("articles/popular/", PopularArticlesViewSet.as_view({'get': 'list'})),
	 path("articles/latest/", LatestArticlesViewSet.as_view({'get': 'list'})),
]