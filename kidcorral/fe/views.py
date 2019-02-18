from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    guardians = request.user.family_legal_guardians.all()
    children = request.user.children.all()
    return render(
        request, "index.html", context={"guardians": guardians, "children": children}
    )
