from django.urls import path

from kidcorral.person import views


urlpatterns = [
    path("", views.create_person, name="person-create"),
    path("<int:person_id>", views.profile, name="profile"),
]
