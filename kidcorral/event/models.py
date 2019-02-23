from django.db import models


from django.utils import timezone


class Room(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_active(cls):
        return Room.objects.filter(active=True)


class Event(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    rooms = models.ManyToManyField(Room, related_name="event_rooms")

    @classmethod
    def get_active(cls):
        now = timezone.now()
        return Event.objects.filter(start_date__lte=now).filter(end_date__gte=now)

    @classmethod
    def get_active_rooms(cls):
        for event in Event.get_active():
            for room in event.rooms.all():
                if room.active:
                    yield room
