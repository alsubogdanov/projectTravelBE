from django.urls import path
from sitecontent.views.public_views import SocialLinkListView, AboutSectionPublicView, ContactSectionPublicView,VideoListPublicView, contact_view
urlpatterns = [
    path("about/", AboutSectionPublicView.as_view(), name="about-section"),
    path("social-links/", SocialLinkListView.as_view(), name="social-links"),
    path('contact/', contact_view, name='contact'),
    path('contactinfo/', ContactSectionPublicView.as_view(), name='contact'),
    path('videos/', VideoListPublicView.as_view(), name='video-list'),
]