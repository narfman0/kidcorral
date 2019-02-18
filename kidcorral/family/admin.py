from django.contrib import admin

from kidcorral.family.models import Family


class FamilyAdmin(admin.ModelAdmin):
    list_display = ["id", "preferred_contact", "legal_guardian_names", "children_names"]

    def legal_guardian_names(self, obj):
        return [person.first_name for person in obj.legal_guardians.all()]

    def children_names(self, obj):
        return [person.first_name for person in obj.children.all()]


admin.site.register(Family, FamilyAdmin)
