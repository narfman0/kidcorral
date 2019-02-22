from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("kidcorral.api.urls")),
    path("family/", include("kidcorral.family.urls")),
    path("person/", include("kidcorral.person.urls")),
    path("visit/", include("kidcorral.visit.urls")),
    path("", include("kidcorral.fe.urls")),
]
