from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.utils import timezone

from kidcorral.event.models import Room
from kidcorral.volunteer import forms
from kidcorral.volunteer.models import Assignment


@login_required
def create_assignment(request):
    if not request.user.volunteer:
        return HttpResponse("Unauthorized", status=401)
    if request.method == "POST":
        form = forms.AssignmentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.volunteer = request.user
            model_instance.save()
            return redirect(reverse("volunteer"))
    form = forms.AssignmentForm()
    form.fields["location"].queryset = Room.get_active()
    return render(request, "create_assignment.html", context={"form": form})


@login_required
def fulfill_assignment(request, assignment_pk):
    assignment = Assignment.objects.get(pk=assignment_pk)
    if assignment.volunteer != request.user:
        return HttpResponse("Unauthorized", status=401)
    assignment.sign_out_time = timezone.now()
    assignment.save()
    return redirect(reverse("volunteer"))


@login_required
def volunteer(request):
    active_assignments = Assignment.objects.filter(
        volunteer=request.user, sign_out_time=None
    )
    if active_assignments.count() == 0:
        return redirect(reverse("create-assignment"))
    # TODO get room:child map and populate in template
    return render(
        request, "volunteer.html", context={"active_assignments": active_assignments}
    )
