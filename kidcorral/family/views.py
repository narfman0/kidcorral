from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from kidcorral.family import forms
from kidcorral.person.models import Person


@login_required
def create(request, family_id):
    if request.method == "POST":
        form = forms.GuardianCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data()["email"]
            guardian = Person.objects.get(email=email)
            family = request.user.family_legal_guardians.all()[0]
            family.guardians.add(guardian)
            return redirect("/")
    form = forms.GuardianCreateForm()
    return render(request, "guardian_create.html", context={"form": form})
