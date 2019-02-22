from django_registration.forms import RegistrationForm

from kidcorral.person.models import Person


class PersonRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = Person
