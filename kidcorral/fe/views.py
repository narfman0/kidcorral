from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from kidcorral.visit.models import Visit


@login_required
def index(request):
    family = request.user.get_family()
    families = request.user.family_legal_guardians.all()
    active_visits = Visit.objects.filter(sign_in_guardian=request.user).exclude(
        sign_out_guardian__isnull=False
    )
    return render(
        request,
        "index.html",
        context={
            "family": family,
            "families": families,
            "active_visits": active_visits,
        },
    )
