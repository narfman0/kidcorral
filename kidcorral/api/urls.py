from django.urls import include, path
from rest_framework import routers

from kidcorral.api import views

router = routers.DefaultRouter()
router.register(r"families", views.FamilyViewSet)
router.register(r"persons", views.PersonViewSet)
router.register(r"visits", views.VisitViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
