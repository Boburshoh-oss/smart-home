from asyncio.log import logger
from rest_framework import serializers
from core.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
        read_only_fields = ('id', 'created_at','owner', 'updated_at')
    
    def create(self, validated_data):
        product_abilty = validated_data['device'].product.num_of_channels
        device = validated_data['device'].channels.all()
        channels_count = device.count()
        logger.info(f"{product_abilty},{device} ,{channels_count}nima bularrrr")
        if channels_count < product_abilty:
            return super().create(validated_data)
        raise serializers.ValidationError({"channels maximum count must be":product_abilty})
    