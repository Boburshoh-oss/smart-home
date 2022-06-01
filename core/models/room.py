from django.db import models
from uuid import uuid4


class Room(models.Model):
    """
    Model representing a room.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200, help_text="Enter a name for this room")
    description = models.TextField(help_text="Enter a description for this room")
    home_id = models.ForeignKey(
        "core.Home", on_delete=models.CASCADE, related_name="rooms"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
