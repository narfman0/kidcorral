from rest_framework import mixins, viewsets

from kidcorral.api import serializers
from kidcorral.family.models import Family
from kidcorral.person.models import Person
from kidcorral.visit.models import Visit

# TODO: i am quite sure for each of these viewsets, an attacker can perform
# create/updates without authz, as there are no permissions classes. While
# they cannot see the information, invalid writes are still bad, so revisit.


class FamilyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Family.objects.none()
    serializer_class = serializers.FamilySerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Family.objects.all()
        return self.request.user.family_legal_guardians.all()


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
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


class VisitViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Visit.objects.none()
    serializer_class = serializers.VisitSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return Visit.objects.all()
        # eventually we will respond with all children's visits for which we
        # are legal guardian
        return self.request.user.visit_originators.all()
