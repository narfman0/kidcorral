from django.db import models


class Family(models.Model):
    preferred_contact = models.ForeignKey(
        "persons.Person", on_delete=models.CASCADE, related_name="preferred_contact"
    )
    legal_guardians = models.ManyToManyField(
        "persons.Person", related_name="legal_guardians"
    )
    children = models.ManyToManyField("persons.Person", related_name="children")

    class Meta:
        verbose_name_plural = "Families"
