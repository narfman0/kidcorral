from django.forms import ModelForm

from kidcorral.person.models import Person


class CreateChildForm(ModelForm):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "birthdate", "allergies", "notes"]
        help_texts = {
            "birthdate": "Birthdate of child in YYYY-MM-DD format. e.g.: 2014-04-04"
        }


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            "first_name",
            "last_name",
            "birthdate",
            "email",
            "phone_number",
            "phone_preferred",
            "allergies",
            "notes",
        ]
