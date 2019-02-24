from django.urls import path

from kidcorral.volunteer import views


urlpatterns = [
    path("assignment", views.create_assignment, name="create-assignment"),
    path(
        "assignment/fulfill/<int:assignment_pk>",
        views.fulfill_assignment,
        name="fulfill-assignment",
    ),
    path("", views.volunteer, name="volunteer"),
]
