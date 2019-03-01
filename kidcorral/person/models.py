from django.db import models
from django.contrib.auth.models import AbstractUser


class Person(AbstractUser):
    allergies = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    phone_number = models.CharField(null=True, blank=True, max_length=64)
    phone_preferred = models.BooleanField(default=True)
    volunteer = models.BooleanField(default=False)

    def is_child(self, person):
        """ Is self the guardian of person? """
        for family in self.family_legal_guardians.all():
            if person in family.children.all():
                return True
        return False

    def name(self):
        return self.first_name + " " + self.last_name

    def contact(self):
        return self.phone_number if self.phone_preferred else self.email

    def __str__(self):
        return self.name()
