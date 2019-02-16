from django.urls import path

from ctrack.families import views

urlpatterns = [path("", views.index, name="index")]
