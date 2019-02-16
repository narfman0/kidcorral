from django.db import models


class Family(models.Model):
    preferred_contact = models.ForeignKey(
        "persons.Person", on_delete=models.CASCADE, related_name="preferred_contact"
    )
    members = models.ManyToManyField("persons.Person")

    class Meta:
        verbose_name_plural = "Families"
