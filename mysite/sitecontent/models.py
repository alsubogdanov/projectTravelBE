from django.db import models


class AboutSection(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(upload_to="about/", null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"AboutSection (updated {self.updated_at})"
class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
   #  image = models.ImageField(upload_to="social_links/", null=True, blank=True)
    svg_file = models.FileField(upload_to="social_links/", null=True, blank=True)

    order = models.PositiveIntegerField(default=0, help_text="Порядок отображения")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name
     

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
     
     
class ContactSection(models.Model):
    """
    Основная секция "Контакты".
    """
    title = models.CharField(max_length=255, default="Get In Touch")
    description = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Branch(models.Model):
    """
    Отдел / филиал.
    """
    contact_section = models.ForeignKey(ContactSection, related_name="branches", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phones = models.CharField(max_length=255)  # можно хранить через запятую
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name



class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='video_thumbnails/')
    url = models.URLField()  # ссылка на YouTube
    order = models.PositiveIntegerField(default=0)  # порядок отображения

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']  # сортировка по порядку

    def __str__(self):
        return self.title
     
     