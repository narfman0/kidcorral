from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Person(AbstractUser):
    allergies = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    phone_preferred = models.BooleanField(default=True)

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
