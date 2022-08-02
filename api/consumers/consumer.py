import json
from channels.generic.websocket import AsyncWebsocketConsumer
from core.models import Channel
import logging
from asgiref.sync import sync_to_async
from core.models.condition import SmartCondition
from core.models.sensor import Sensor
import asyncio
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# from channels.auth import http_session_user, channel_session_user, channel_session_user_from_http
logger = logging.getLogger('consumer')

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user = self.scope["user"]
        self.room_name =  "topic_room"
        if user.username:
            self.room_group_name = 'topic_group'
        else:
            self.room_group_name =  "adashib_qol"
        # self.room_group_name = 'chat_%s' % self.room_name
        logger.info("Resived from group name: {}".format(self.room_group_name))
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        
        
        await self.channel_layer.group_add("mqttgroup", self.channel_name)
        
        # sensors = await database_sync_to_async(Sensor.objects.filter)(owner=user)
        
        
        # sensors = await self.get_all_sensors(user)
        
        subscribes = await self.get_all_channels_sensors(user)
        logger.info("Sensors: {}".format(subscribes))
        
        
        
        try:
            tasks = [self.channel_layer.send(url[0],url[1]) for url in subscribes]
            await asyncio.wait(tasks)
        except Exception as e:
            logger.error(e)
            
        await self.accept()
        logger.info("Connected to websocket")
        logger.info("Qanaqa user bu: {}".format(user.username))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        
    async def receive(self, text_data):
        
        user = self.scope["user"]
        logger.info("Message user from websocket: {}".format(user))
        try:
            text_data_json = json.loads(text_data)
        
        # type = text_data_json["type"]
            message = text_data_json["message"]
            topic = text_data_json["topic"]
            logger.info("Message received from websocket: {}".format(message))
            logger.info("Topic received from websocket: {}".format(topic))
            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name, {"type": "chat_message", "message": message}
            )
            
            # Publish on mqtt too
            await self.channel_layer.send(
                "mqtt",
                {
                    "type": "mqtt_publish",
                    "publish": {  # These form the kwargs for mqtt.publish
                        "topic": topic,
                        "payload": message,
                        "qos": 2,
                        "retain": False,
                    },
                },
            )
        except:
            pass
     
           
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        
        # Send message to WebSocket
        # await self.send(text_data=json.dumps({"message": message}))

    # Receive message from mqtt group and send to websocket
    async def mqtt_message(self, event):
        message = event["message"]
        topic = message["topic"]
        payload = message["payload"]
        
        user = self.scope["user"]
        logger.info("Received message from mqtt: {},topic:{}".format(payload,topic))
        #from mqtt status 1 or 0 save database
        if user.username:
            pass
        else:
            await self.channel_mqtt(payload,topic)
            #from mqtt save database
            
            await self.sensor_mqtt(payload,topic,user)
        # chan = await database_sync_to_async(self.get_channel)()
        # if payload == "ON" or payload == b'ON':
        #     # chan.status__id = 2
        #     # chan.status_id = 2
        #     chan.status = await database_sync_to_async(Status.objects.get)(status='on')
        # else:
        #     chan.status = await database_sync_to_async(Status.objects.get)(status='off')
        #     # chan.status__id = 1
        #     # chan.status_id = 1

        # await database_sync_to_async(chan.save)()
        sensor_or_channel = await self.get__channel_or_sensor(topic)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": payload,"result":sensor_or_channel.id}))

    #from user to device switch on or off
    @sync_to_async
    def channel_mqtt(self, message,topic):
        logger.info(f"{message}/{topic} channel_mqtt")
        try:
            topic = str(topic)[1:]
            channel = Channel.objects.get(topic_name = topic)   
            # logger.info("Received channel from base: {}".format(channel))
            if message == 0:
                state = False
                channel.state = state
            elif message == 1:
                state = True
                channel.state = state
            
            channel.save()
        except Exception as e:
            logger.error(e)
        
        

    
    @sync_to_async
    def sensor_mqtt(self, payload,  topic,user):
        logger.info(f"{payload}/{topic} sensor_mqtt")
        topic = str(topic)[1:]
        try:
            smart_conditions = SmartCondition.objects.filter(condition__timer=None,condition__sensor_status__sensor__topic_name=topic)
            if user.username:
                pass
            else:
                for sc in smart_conditions:
                    a = sc.condition.sensor_status.above
                    b = sc.condition.sensor_status.below
                    if int(payload) > a or int(payload) < b:
                        channels = sc.channel.all()
                        sana = 0
                        for channel in channels:
                            sana += 1
                            notification = {
                                            "type": "mqtt_publish",
                                            "publish": {  # These form the kwargs for mqtt.publish
                                                "topic": channel.topic_name,
                                                "payload": f"{channel.topic_name},{sana}",
                                                "qos": 2,
                                                "retain": False,
                                            },
                                        }
                            async_to_sync(self.channel_layer.send)("mqtt", notification)
                        
            # for sensor_state in smart_conditions:
            #     if sensor_state.condtion.sensor_status.sensor.topic_name == topic:
                    
        except Exception as e:
            logger.error(e)
        try:
            if user.username:
                pass
            else:
                sensor = Sensor.objects.get(topic_name=topic)
                sensor.state += f" {payload}"
                array_state = sensor.state.split()
                if len(array_state)>10:
                    del array_state[0]
                sensor.state = ' '.join(array_state)
                sensor.save()
        except Exception as e:
            logger.error(e)
    
    @sync_to_async
    def get_all_channels_sensors(self,user):
        subscribes = []
        try:
            
            sensors = Sensor.objects.all()
            for sensor in sensors:
                subscribes.append([
                "mqtt",
                {
                    "type": "mqtt_subscribe",
                    "topic": f"1{sensor.topic_name}",
                    "group": "mqttgroup",
                },
            ])
        except Exception as e:
            
            logger.error(f"{e} sensor topilmadi")
        try: 
            
            channels = Channel.objects.all()
            for channel in channels:
                subscribes.append([
                    "mqtt",
                    {
                        "type": "mqtt_subscribe",
                        "topic": f"1{channel.topic_name}",
                        "group": "mqttgroup",
                    },
                ])
        except Exception as e:
            
            logger.error(f"{e} channel topilmadi")
        return subscribes
    
    
    @sync_to_async
    def get__channel_or_sensor(self,topic):
            topic = str(topic)[1:]
            sensor = None
            try:
                sensor = Sensor.objects.get(topic_name = topic)
            except Exception as e:
                logger.error(e)
            try:
                sensor = Channel.objects.get(topic_name = topic)
            except Exception as e:
                logger.error(e)
            # logger.info("Received channel from base: {}".format(channel))
            return sensor  
        
        
        
             
        
    # def get_sensor(self,topic):
    #     return Sensor.objects.get(topic_name=topic)
        

