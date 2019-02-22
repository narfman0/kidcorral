from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from kidcorral.family.models import Family
from kidcorral.person import forms
from kidcorral.person.models import Person


@login_required
def create_person(request, family_id):
    family = Family.objects.get(pk=family_id)
    if family not in request.user.family_legal_guardians.all():
        return HttpResponse("Unauthorized", status=401)
    if request.method == "POST":
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            child = form.save()
            family.children.add(child)
            return redirect("/")
    form = forms.PersonForm()
    return render(
        request, "create_person.html", context={"form": form, "family": family}
    )


@login_required
def profile(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    if person != request.user and not request.user.is_child(person):
        return HttpResponse("Unauthorized", status=401)
    if request.method == "POST":
        form = forms.PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = forms.PersonForm(instance=person)
    return render(request, "profile.html", context={"person": person, "form": form})
