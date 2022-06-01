from rest_framework import serializers
from core.models import Room, Home


class RoomSerializer(serializers.ModelSerializer):
    home_id = serializers.SlugRelatedField(
        read_only=False,
        queryset=Home.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Room
        fields = ('id', 'name', 'description', 'home_id', 'created_at')
