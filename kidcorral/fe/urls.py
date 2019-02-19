from django.urls import path

from kidcorral.fe import views


urlpatterns = [
    path("", views.index, name="index"),
    path("signin/<int:person_id>", views.signin, name="signin"),
    path("signout/<int:visit_id>", views.signout, name="signout"),
]
