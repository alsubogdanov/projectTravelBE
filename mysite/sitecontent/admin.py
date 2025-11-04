
# Register your models here.
from django.contrib import admin
from .models import SocialLink, AboutSection,ContactMessage, Branch, ContactSection, Video


# @admin.register(AboutSection)
# class AboutSectionAdmin(admin.ModelAdmin):
#     list_display = ("title", "updated_at")
#     readonly_fields = ("updated_at",)


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "order")
    list_editable = ("order",)
    


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "updated_at")
    readonly_fields = ("updated_at",)
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    
class BranchInline(admin.StackedInline):
    model = Branch  # говорим, что это дочерняя модель
    extra = 1       # сколько пустых форм показывать по умолчанию
  
@admin.register(ContactSection)
class ContactSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email', 'address', 'updated_at']
    inlines = [BranchInline]  # подключаем Inline
    
    
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title',)