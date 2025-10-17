# articles/admin.py

from django.contrib import admin
from .models import Article # Импортируем нашу модель Post

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "create_date")
    search_fields = ("title", "author")
    list_filter = ("create_date",)