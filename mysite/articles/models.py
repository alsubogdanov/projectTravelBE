# articles/models.py

from django.db import models
from django.utils import timezone # (Для даты публикации)
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=200)   # заголовок
    img = models.ImageField(upload_to="articles/", blank=True, null=True)  # картинка
    author = models.CharField(max_length=100)  # автор
    create_date = models.DateField(auto_now_add=True)  # дата создания
    content = RichTextField()   # <-- заменили TextField на RichTextField

    def __str__(self):
        return self.title
     
     
     
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    #Показывает имя автора и первые 30 символов комментария.
        return f"{self.name} - {self.text[:30]}"