from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Person(AbstractUser):
    allergies = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    phone_preferred = models.BooleanField(default=True)


class Family(models.Model):
    preferred_contact = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="preferred_contact"
    )
    members = models.ManyToManyField(Person)

    class Meta:
        verbose_name_plural = "Families"
