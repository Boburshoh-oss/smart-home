from django.db import models
from uuid import uuid4


class Channel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200) # lampa
    description = models.TextField(max_length=200)
    room = models.ForeignKey(
        "core.Room", on_delete=models.CASCADE, related_name="channels"
    )
    status = models.ForeignKey(
        "core.Status", on_delete=models.CASCADE, related_name="channels"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super().save(*args, **kwargs)


class Status(models.Model):
    ON = "on"
    OFF = "off"
    STATUS_CHOICES = (
        (ON, "on"),
        (OFF, "off"),
    )

    status = models.CharField(
        max_length=3, choices=STATUS_CHOICES, default=ON, unique=True
    )

    def __str__(self):
        return self.status

    class Meta:
        db_table = "Statuses"
        verbose_name = "Status"
        verbose_name_plural = "Statuses"
