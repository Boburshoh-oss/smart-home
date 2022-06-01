from django.db import models
from uuid import uuid4


class Sensor(models.Model):
    """
    A sensor is a device that can be used to measure a certain thing.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    room = models.ForeignKey(
        "core.Room", on_delete=models.CASCADE, related_name="sensors"
    )
    type = models.CharField(
        max_length=100,
        choices=[
            ("temperature", "Temperature"),
            ("humidity", "Humidity"),
            ("light", "Light"),
            ("motion", "Motion"),
        ],
        default="temperature",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
