from django.db import models



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