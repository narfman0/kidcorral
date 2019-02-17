from django.urls import include, path
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

from kidcorral.api import views

router = routers.DefaultRouter()
router.register(r"families", views.FamilyViewSet)
router.register(r"persons", views.PersonViewSet)
router.register(r"visits", views.VisitViewSet)
schema_view = get_schema_view(title="kidcorral API")
swagger_view = get_swagger_view(title="kidcorral API")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("schema/", schema_view),
    path("swagger/", swagger_view),
]
