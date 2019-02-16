from django.contrib import admin

from kidcorral.families.models import Family, Person


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["preferred_contact", "member_names"]

    def member_names(self, obj):
        return [member.first_name for member in obj.members.all()]


class PersonAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "phone_number"]


admin.site.register(Family, FamilyAdmin)
admin.site.register(Person, PersonAdmin)
