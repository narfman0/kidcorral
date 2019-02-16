from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Person(AbstractUser):
    allergies = models.TextField(blank=True)
    phone_number = PhoneNumberField(blank=True)
    phone_preferred = models.BooleanField(default=True)


class Family(models.Model):
    preferred_contact = models.ForeignKey(
        Person, on_delete=models.CASCADE, related_name="preferred_contact"
    )
    members = models.ManyToManyField(Person)
