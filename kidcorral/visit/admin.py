from django.contrib import admin

from kidcorral.visit.models import Visit


class VisitAdmin(admin.ModelAdmin):
    list_display = ["id", "child", "sign_in_time", "sign_out_time", "location"]


admin.site.register(Visit, VisitAdmin)
