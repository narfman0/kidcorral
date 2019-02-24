from django.contrib import admin

from kidcorral.volunteer.models import Assignment


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ["id", "volunteer", "location"]


admin.site.register(Assignment, AssignmentAdmin)
