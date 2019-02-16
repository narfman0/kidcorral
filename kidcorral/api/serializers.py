from rest_framework import serializers

from kidcorral.person.models import Person
from kidcorral.visit.models import Visit


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ("username", "email", "allergies", "notes", "phone_number")


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
