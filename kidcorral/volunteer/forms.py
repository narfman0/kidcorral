from django.forms import ModelForm

from kidcorral.volunteer.models import Assignment


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ["location", "notes"]
