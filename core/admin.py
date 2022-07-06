from django.contrib import admin
from core.models import User, Channel, Device, Home, Sensor, Product, SmartCondition,Condition,SensorState


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     fields = ("name", "phone_number", "email", "username", "password", "is_staff", "is_superuser")
#     list_display = ("username", "name", "email", "is_staff", "phone_number")
#     list_filter = ("username", "name", "is_staff", "phone_number")
#     search_fields = ("username", "name", "phone_number")
#     ordering = ("username", "email", "name")
admin.site.register(SmartCondition)
admin.site.register(SensorState)
admin.site.register(Condition)
admin.site.register(User)
@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)
    ordering = ("name",)



    
class ChannelItemInline(admin.TabularInline):
    model = Channel
    extra = 0

class SensorItemInline(admin.TabularInline):
    model = Sensor
    extra = 0


class DeviceAdmin(admin.ModelAdmin):
    inlines = [ChannelItemInline,SensorItemInline]
    list_display = ("owner","name", "product", "home","created_at","updated_at")
    list_filter = ("name", "product", "home","owner")
    search_fields = ("name", "product", "home")
    ordering = ("name", "product", "home")
    class Meta:
        model = Device
admin.site.register(Device,DeviceAdmin)

admin.site.register(Sensor)
admin.site.register(Product)
admin.site.register(Home)
