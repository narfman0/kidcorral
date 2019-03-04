from django.db import models

from kidcorral.family.models import Family


class Visit(models.Model):
    child = models.ForeignKey(
        "person.Person", on_delete=models.CASCADE, related_name="visit_targets"
    )
    location = models.ForeignKey(
        "event.Room", blank=True, null=True, on_delete=models.CASCADE
    )
    notes = models.TextField(null=True, blank=True)
    sign_in_guardian = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="visit_signin_guardians",
        blank=True,
        null=True,
    )
    sign_in_time = models.DateTimeField(null=True, blank=True)
    sign_in_volunteer = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="visit_signin_volunteers",
        blank=True,
        null=True,
    )
    sign_out_guardian = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="visit_signout_guardians",
        blank=True,
        null=True,
    )
    sign_out_time = models.DateTimeField(null=True, blank=True)
    sign_out_volunteer = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="visit_signout_volunteers",
        blank=True,
        null=True,
    )

    def family(self):
        return Family.objects.get(children__pk=self.child.pk)

    def preferred_contact(self):
        return self.family().preferred_contact
