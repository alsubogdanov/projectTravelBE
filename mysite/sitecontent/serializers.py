from rest_framework import serializers
from .models import SocialLink, AboutSection



class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"
        
        

class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = ["id", "title", "content", "image", "updated_at"]
        read_only_fields = ["id", "updated_at"]