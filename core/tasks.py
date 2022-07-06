from asyncio.log import logger
from config.celery import app
# from core.models.channel import Channel
from core.models.condition import SmartCondition
from django.utils import dateformat
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@app.task() 
def mqtt_task_scheduale():
    start_time = dateformat.format(datetime.datetime.now(), 'H:i:s')
    end_time = dateformat.format(datetime.datetime.now()+datetime.timedelta(minutes=1), 'H:i:s')
    
    scs = SmartCondition.objects.filter(condition__timer__range=[start_time,end_time])
    channel_layer = get_channel_layer()
    
    for sc in scs:
        for chan in sc.channel.all():
            notification = {
                    "type": "mqtt_publish",
                    "publish": {  # These form the kwargs for mqtt.publish
                        "topic": chan.topic_name,
                        "payload": sc.status,
                        "qos": 2,
                        "retain": False,
                    },
                }
            async_to_sync(channel_layer.send)("mqtt", notification)
    logger.info(f"{scs},smart conditions")
    
        
    logger.info(f"{end_time},time condition")
    return {"result":True}

