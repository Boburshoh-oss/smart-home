from django.db import models

class SmartCondition(models.Model):
    owner = models.ForeignKey("core.User",on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200)
    condition = models.ForeignKey("core.Condition",on_delete=models.CASCADE)
    device = models.ForeignKey("core.Device",on_delete=models.CASCADE)
    
    channel =  models.ManyToManyField("core.Channel")
    
    status = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
    
class Condition(models.Model):
    timer = models.TimeField(blank=True,null=True)
    sensor_status = models.ForeignKey('core.SensorState',on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return f"{self.timer} / {self.sensor_status}"
    
class SensorState(models.Model):
    sensor = models.ForeignKey('core.Sensor',on_delete=models.CASCADE)
    above = models.IntegerField()
    below = models.IntegerField()
    def __str__(self):
        return f"{self.above} <{self.sensor}< {self.below}"