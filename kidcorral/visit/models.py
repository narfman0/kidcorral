from django.db import models


class Visit(models.Model):
    originator = models.ForeignKey(
        "person.Person", on_delete=models.CASCADE, related_name="visit_originators"
    )
    child = models.ForeignKey(
        "person.Person", on_delete=models.CASCADE, related_name="visit_targets"
    )
    sign_in = models.DateTimeField(auto_now_add=True, blank=True)
    sign_out = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
