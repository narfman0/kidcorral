from django.contrib import admin

from kidcorral.person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "phone_number"]


admin.site.register(Person, PersonAdmin)
