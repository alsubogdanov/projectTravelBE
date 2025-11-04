from rest_framework import serializers
from .models import SocialLink, AboutSection,Branch,ContactSection,Video



class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"
        
        

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = ["id", "title", "content", "image", "updated_at"]
        read_only_fields = ["id", "updated_at"]
        
        
class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id', 'name', 'address', 'phones', 'email']

class ContactSectionSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)  # подключаем филиалы

    class Meta:
        model = ContactSection
        fields = ['id', 'title', 'description', 'phone', 'email', 'address', 'branches', 'updated_at']
        
        


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'thumbnail', 'url', 'order']