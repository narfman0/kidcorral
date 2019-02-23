from django.contrib import admin

from kidcorral.event import models


class RoomAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "active"]


class EventAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "start_date", "end_date", "room_names"]

    def room_names(self, obj):
        return [room.name for room in obj.rooms.all()]


admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Event, EventAdmin)
