from django.urls import path

from kidcorral.visit import views


urlpatterns = [
    path("tag/<int:visit_id>", views.tagcreate, name="create-tag"),
    path("signin/<int:person_id>", views.signin, name="signin"),
    path("signout/<int:visit_id>", views.signout, name="signout"),
]
