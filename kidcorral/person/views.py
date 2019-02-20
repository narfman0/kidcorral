from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from kidcorral.person import forms
from kidcorral.person.models import Person


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
