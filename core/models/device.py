from django.db import models


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    product = models.ForeignKey(
        "core.Product", on_delete=models.SET_NULL, related_name="devices", null=True
    )
    home = models.ForeignKey(
        "core.Home", on_delete=models.CASCADE, related_name="devices"
    )
    channels = models.ManyToManyField("core.Channel")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
