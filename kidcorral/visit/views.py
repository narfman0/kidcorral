from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from kidcorral.person.models import Person
from kidcorral.visit import forms
from kidcorral.visit.models import Visit


@login_required
def signin(request, person_id):
    child = get_object_or_404(Person, id=person_id)
    if request.method == "POST":
        form = forms.VisitForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.child = child
            model_instance.sign_in_guardian = request.user
            model_instance.sign_in_time = timezone.now()
            model_instance.save()
            return redirect("/")
    form = forms.VisitForm()
    return render(request, "signin.html", context={"child": child, "form": form})


@login_required
def signout(request, visit_id):
    visit = get_object_or_404(Visit, id=visit_id)
    visit.sign_out_guardian = request.user
    visit.sign_out_time = timezone.now()
    visit.save()
    return redirect("/")