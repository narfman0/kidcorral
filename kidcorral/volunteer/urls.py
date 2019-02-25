from django.urls import path

from kidcorral.volunteer import views


urlpatterns = [
    path(
        "acknowledge/signin/<int:visit_pk>",
        views.acknowledge_child_signin,
        name="acknowledge-child-signin",
    ),
    path(
        "acknowledge/signout/<int:visit_pk>",
        views.acknowledge_child_signout,
        name="acknowledge-child-signout",
    ),
    path("assignment", views.create_assignment, name="create-assignment"),
    path(
        "assignment/fulfill/<int:assignment_pk>",
        views.fulfill_assignment,
        name="fulfill-assignment",
    ),
    path("", views.volunteer, name="volunteer"),
]
