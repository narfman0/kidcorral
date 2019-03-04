import string
import random

from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    allergies = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=64)
    phone_preferred = models.BooleanField(default=True)
    volunteer = models.BooleanField(default=False)
    birthdate = models.DateField(null=True, blank=True)

    def is_child(self, person):
        """ Is self the guardian of person? """
        for family in self.family_legal_guardians.all():
            if person in family.children.all():
                return True
        return False

    def name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        if self.first_name:
            return self.first_name
        if self.last_name:
            return self.last_name
        return self.username

    def contact(self):
        return self.phone_number if self.phone_preferred else self.email

    def __str__(self):
        return self.name()

    @classmethod
    def generate_username(cls, first_name, last_name):
        suffix = "".join(
            random.choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(5)
        )
        return f"{first_name}.{last_name}.{suffix}"
