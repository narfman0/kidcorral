from django.contrib import admin

from kidcorral.families.models import Family


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["preferred_contact", "member_names"]

    def member_names(self, obj):
        return [member.first_name for member in obj.members.all()]


admin.site.register(Family, FamilyAdmin)
