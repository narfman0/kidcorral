from rest_framework import generics, mixins, viewsets

from kidcorral.api import serializers
from kidcorral.family.models import Family
from kidcorral.person.models import Person
from kidcorral.visit.models import Visit


class FamilyViewSet(viewsets.ModelViewSet):
    queryset = Family.objects.none()
    serializer_class = serializers.FamilySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Family.objects.all()
        return self.request.user.family_legal_guardians.all()


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.none()
    serializer_class = serializers.PersonSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Person.objects.all()
        people = []
        for family in self.request.user.family_legal_guardians.all():
            people.extend(family.legal_guardians.all())
            people.extend(family.children.all())
        return people


class VisitViewSet(viewsets.ModelViewSet):
    queryset = Visit.objects.none()
    serializer_class = serializers.VisitSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Visit.objects.all()
        # initially we respond with all visits for which we are originator
        # eventually we will respond with all children's visits for which we
        # are legal guardian
        return self.request.user.visit_originators.all()
