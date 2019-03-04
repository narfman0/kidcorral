from django import forms


class FamilyCreateForm(forms.Form):
    family_name = forms.CharField(max_length=100)


class GuardianCreateForm(forms.Form):
    email = forms.EmailField()
