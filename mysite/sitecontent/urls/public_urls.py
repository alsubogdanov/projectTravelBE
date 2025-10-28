from django.urls import path
from sitecontent.views.public_views import SocialLinkListView, AboutSectionPublicView
urlpatterns = [
    path("about/", AboutSectionPublicView.as_view(), name="about-section"),
    path("social-links/", SocialLinkListView.as_view(), name="social-links"),
]