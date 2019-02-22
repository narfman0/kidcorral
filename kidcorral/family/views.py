from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from kidcorral.family import forms
from kidcorral.family.models import Family
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
    return render(request, "associate_guardian.html", context=context)


@login_required
def create_family(request):
    if request.method == "POST":
        form = forms.FamilyCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            family = Family.objects.create(name=name, preferred_contact=request.user)
            family.legal_guardians.add(request.user)
            return redirect("/")
    form = forms.FamilyCreateForm()
    return render(request, "create_family.html", context={"form": form})
