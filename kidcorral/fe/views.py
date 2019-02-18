from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    families = request.user.family_legal_guardians.all()
    return render(request, "index.html", context={"families": families})
