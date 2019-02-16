from rest_framework import viewsets

from kidcorral.api import serializers
from kidcorral.persons.models import Person
from kidcorral.visit.models import Visit


class PersonsViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer


class VisitsViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.all()
    serializer_class = serializers.VisitSerializer
