from django.urls import path

from kidcorral.person import views


urlpatterns = [
    path("", views.create, name="person-create"),
    path("<int:person_id>", views.profile, name="profile"),
]
