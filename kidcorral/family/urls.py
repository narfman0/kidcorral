from django.urls import path

from kidcorral.family import views


urlpatterns = [
    path(
        "<int:family_id>/guardian", views.associate_guardian, name="guardian-associate"
    ),
    path("", views.create_family, name="create-family"),
]
