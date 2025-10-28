
# Register your models here.
from django.contrib import admin
from .models import SocialLink, AboutSection


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