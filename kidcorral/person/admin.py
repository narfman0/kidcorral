from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from kidcorral.person.models import Person


class PersonForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].help_text = (
            "Raw passwords are not stored, so there is no way to see "
            "this user's password."
        )

    class Meta:
        model = Person
        fields = "__all__"


class PersonAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_staff",
        "volunteer",
    ]
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
    form = PersonForm


admin.site.register(Person, PersonAdmin)
