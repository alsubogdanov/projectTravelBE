#sitecontent/urls/admin_urls.py
from django.urls import path
from ..views.admin_views import AboutSectionAdminView

urlpatterns = [
    path("about/", AboutSectionAdminView.as_view(), name="about-admin"),
]