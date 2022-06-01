from django.contrib import admin
from core.models import User, Channel, Device, Home, Status, Sensor, Room, Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ("name", "phone_number", "email", "username", "password", "is_staff", "is_superuser")
    list_display = ("username", "name", "email", "is_staff", "phone_number")
    list_filter = ("username", "name", "is_staff", "phone_number")
    search_fields = ("username", "name", "phone_number")
    ordering = ("username", "email", "name")


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "room")
    list_filter = ("name", "status", "room")
    search_fields = ("name", "status", "room")
    ordering = ("name", "room")


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "product", "home")
    list_filter = ("name", "product", "home")
    search_fields = ("name", "product", "home")
    ordering = ("name", "product", "home")


admin.site.register(Status)
admin.site.register(Sensor)
admin.site.register(Room)
admin.site.register(Product)
admin.site.register(Home)
