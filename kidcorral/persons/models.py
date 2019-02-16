from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Person(AbstractUser):
    allergies = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    phone_preferred = models.BooleanField(default=True)
