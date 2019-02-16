from rest_framework import serializers

from kidcorral.family.models import Family
from kidcorral.person.models import Person
from kidcorral.visit.models import Visit


class FamilySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Family
        fields = "__all__"


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
            "email",
            "allergies",
            "notes",
            "phone_number",
        )


class VisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visit
        fields = "__all__"
