from django.db import models


class Family(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    preferred_contact = models.ForeignKey(
        "person.Person",
        on_delete=models.CASCADE,
        related_name="family_preferred_contact",
    )
    legal_guardians = models.ManyToManyField(
        "person.Person", related_name="family_legal_guardians"
    )
    children = models.ManyToManyField("person.Person", related_name="children")

    class Meta:
        verbose_name_plural = "Families"
