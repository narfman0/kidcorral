from django.urls import path
from django_registration.backends.one_step.views import RegistrationView

from kidcorral.fe import forms, views


urlpatterns = [
    path(
        "register/",
        RegistrationView.as_view(form_class=forms.PersonRegistrationForm),
        name="person_register",
    ),
    path("", views.index, name="index"),
]
