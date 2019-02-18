from django.urls import path

from kidcorral.fe import views


urlpatterns = [path("", views.index, name="index")]
