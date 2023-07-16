from django.db import models
from django.utils.timezone import now

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return f"{self.name}"

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=now, editable=False)

    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000) #specifying the room id where this message belongs to

    def __str__(self) -> str:
        return f"{self.date}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "value": self.value,
            "user": self.user,
            "room": self.room,
            "date": self.date.strftime("%d/%m/%Y %H:%M ")
        }