from django import forms


class GuardianCreateForm(forms.Form):
    email = forms.EmailField(label="Guardian email")
