from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from kidcorral.family import forms
from kidcorral.person.models import Person


@login_required
def associate_guardian(request, family_id):
    if request.method == "POST":
        form = forms.GuardianCreateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            guardian = Person.objects.get(email=email)
            family = request.user.get_family()
            family.legal_guardians.add(guardian)
            return redirect("/")
    form = forms.GuardianCreateForm()
    context = dict(family=request.user.get_family(), form=form)
    return render(request, "guardian_associate.html", context=context)
