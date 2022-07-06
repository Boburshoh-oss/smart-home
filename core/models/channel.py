from django.db import models
from uuid import uuid4


class Channel(models.Model):
    owner = models.ForeignKey(to='core.User', on_delete=models.CASCADE, blank=True,null=True)
    name = models.CharField(max_length=200,unique=True) # lampa
    description = models.TextField(max_length=200,blank=True,null=True)
    # room = models.ForeignKey(
    #     "core.Room", on_delete=models.CASCADE, related_name="channels"
    # )
    device = models.ForeignKey('core.Device',on_delete=models.CASCADE,null=True,related_name="channels")
    topic_name = models.CharField(max_length=200,unique=True,blank=True,null=True)
    state = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        #HomeName/DeviceName/ChannelName
        # self.topic_name = f"{self.device.home}/{self.device}/{self.name}"
        self.name = self.name.lower()
        super().save(*args, **kwargs)



