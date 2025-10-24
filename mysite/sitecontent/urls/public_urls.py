from django.urls import path
from sitecontent.views.public_views import SocialLinkListView

urlpatterns = [
   #  path("about/", AboutSectionView.as_view(), name="about-section"),
    path("social-links/", SocialLinkListView.as_view(), name="social-links"),
]