from django.urls import path

from kidcorral.volunteer import views


urlpatterns = [
    path("assignment", views.create_assignment, name="create-assignment"),
    path("", views.volunteer, name="volunteer"),
]
