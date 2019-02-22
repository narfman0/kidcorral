from django.urls import path

from kidcorral.person import views


urlpatterns = [
    path("<int:person_id>/profile", views.profile, name="profile"),
    path("<int:family_id>", views.create_person, name="create-person"),
]
