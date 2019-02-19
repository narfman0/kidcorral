from django.forms import ModelForm

from kidcorral.visit.models import Visit


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ["location", "notes"]
