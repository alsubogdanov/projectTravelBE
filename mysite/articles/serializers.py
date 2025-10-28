from rest_framework import serializers
from .models import Article
from .models import Comment
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        
        
        
       


class CommentSerializer(serializers.ModelSerializer):
		#дополнительное поле, которое не существует напрямую в модели, а будет вычисляться через метод get_replies.
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        #список полей, которые будут отображаться в JSON.
        fields = ['id', 'article', 'parent', 'name', 'email', 'text', 'date', 'replies']

    def get_replies(self, obj):
        serializer = CommentSerializer(obj.replies.all(), many=True)
        return serializer.data