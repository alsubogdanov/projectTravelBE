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