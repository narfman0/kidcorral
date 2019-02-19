from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone

from kidcorral.fe import forms
from kidcorral.person.models import Person
from kidcorral.visit.models import Visit


@login_required
def index(request):
    families = request.user.family_legal_guardians.all()
    active_visits = Visit.objects.filter(sign_in_guardian=request.user).exclude(
        sign_out_guardian__isnull=False
    )
    return render(
        request,
        "index.html",
        context={"families": families, "active_visits": active_visits},
    )


@login_required
def signin(request, person_id):
    child = Person.objects.get(pk=person_id)
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
    visit = Visit.objects.get(pk=visit_id)
    visit.sign_out_guardian = request.user
    visit.sign_out_time = timezone.now()
    visit.save()
    return redirect("/")
