from django.db import models


class Assignment(models.Model):
    volunteer = models.ForeignKey(
        "person.Person", on_delete=models.CASCADE, related_name="assignment_volunteer"
    )
    location = models.ForeignKey(
        "event.Room", blank=True, null=True, on_delete=models.CASCADE
    )
    notes = models.TextField(null=True, blank=True)
    sign_in_time = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    sign_out_time = models.DateTimeField(null=True, blank=True)
