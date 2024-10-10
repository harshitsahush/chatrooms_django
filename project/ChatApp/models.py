from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self) -> str:
        return f"By : {self.user} in room : {self.room}"