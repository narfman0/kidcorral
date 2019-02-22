from django.urls import path

from kidcorral.family import views


urlpatterns = [
    path("<int:family_id>/guardian", views.create_guardian, name="guardian-create")
]
