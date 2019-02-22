from django import forms


class FamilyCreateForm(forms.Form):
    name = forms.CharField(max_length=100)


class GuardianCreateForm(forms.Form):
    email = forms.EmailField(label="Guardian email")
