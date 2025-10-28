# articles/admin.py

from django.contrib import admin
from .models import Article, Comment # Импортируем нашу модель Post

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('name', 'email', 'text', 'parent', 'date')
    readonly_fields = ('date',)
    
    
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "create_date")
    search_fields = ("title", "author")
    list_filter = ("create_date",)
    inlines = [CommentInline]
    

    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'parent', 'short_text', 'date')
    list_filter = ('article', 'date')
    search_fields = ('name', 'email', 'text')
    ordering = ('-date',)

    def short_text(self, obj):
        return obj.text[:50]
    short_text.short_description = 'Comment'
    
