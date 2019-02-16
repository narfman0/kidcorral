from django.db import models


class Visit(models.Model):
    originator = models.ForeignKey(
        "persons.Person", on_delete=models.CASCADE, related_name="originator"
    )
    child = models.ForeignKey(
        "persons.Person", on_delete=models.CASCADE, related_name="target"
    )
    sign_in = models.DateTimeField(auto_now_add=True, blank=True)
    sign_out = models.DateTimeField(null=True, blank=True)
    location = models.CharField(max_length=200)
    notes = models.TextField(null=True, blank=True)
