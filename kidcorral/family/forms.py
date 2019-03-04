from django import forms


class FamilyCreateForm(forms.Form):
    family_name = forms.CharField(
        max_length=100, help_text="Last name of family or distinct nickname, e.g. Smith"
    )


class GuardianCreateForm(forms.Form):
    email = forms.EmailField()
