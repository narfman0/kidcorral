from django.urls import path

from kidcorral.visit import views


urlpatterns = [
    path("signin/<int:person_id>", views.signin, name="signin"),
    path("signout/<int:visit_id>", views.signout, name="signout"),
]
