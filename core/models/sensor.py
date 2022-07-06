from django.db import models
from uuid import uuid4


class Sensor(models.Model):
    """
    A sensor is a device that can be used to measure a certain thing.
    """
    owner = models.ForeignKey(to='core.User', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    state = models.CharField(max_length=255)
    device = models.ForeignKey('core.Device',on_delete=models.CASCADE,null=True,related_name="sensors")
    topic_name = models.CharField(max_length=200,unique=True,blank=True,null=True)
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

    def save(self, *args, **kwargs):
        #user-email/HomeName/DeviceName/Sensorname
        # self.topic_name = f"{self.device.home}/{self.device}/{self.name}"
        self.name = self.name.lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    
