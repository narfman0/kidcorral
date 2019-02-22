from django.urls import path

from kidcorral.person import views


urlpatterns = [
    path("<int:family_id>", views.create_person, name="create-person"),
    path("<int:person_id>", views.profile, name="profile"),
]
