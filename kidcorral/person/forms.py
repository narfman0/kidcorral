from django.forms import ModelForm

from kidcorral.person.models import Person


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "phone_preferred",
            "allergies",
            "notes",
        ]
