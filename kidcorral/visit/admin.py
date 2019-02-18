from django.contrib import admin

from kidcorral.visit.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ["id", "originator", "child", "sign_in", "sign_out", "location"]


admin.site.register(Visit, VisitAdmin)
