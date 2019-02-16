from rest_framework import viewsets

from kidcorral.api import serializers
from kidcorral.person.models import Person
from kidcorral.visit.models import Visit


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = serializers.VisitSerializer
