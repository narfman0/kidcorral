from django.forms import ModelForm

from kidcorral.visit.models import Visit


class VisitForm(ModelForm):
    class Meta:
        model = Visit
        fields = ["location", "notes"]
        help_texts = {
            "notes": "Visit specific notes like 'child is potty training' "
            + "or 'do not let her father pick her up'"
        }
