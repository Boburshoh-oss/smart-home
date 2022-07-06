from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from core.models.condition import SmartCondition
from .models import Channel, Sensor
from uuid import uuid4
import datetime
from datetime import datetime, timedelta
from asyncio.log import logger



@receiver(post_save, sender=Channel)
def create_channel_topic(sender, instance, created, **kwargs):
    if created:
        instance.topic_name = f"{instance.device.home}{uuid4()}/{instance.device}/{instance.name}"
        instance.save()
        
@receiver(post_save, sender=Sensor)
def create_channel_topic(sender, instance, created, **kwargs):
    if created:
        instance.topic_name = f"{instance.device.home}{uuid4()}/{instance.device}/{instance.name}"
        instance.save()
        
