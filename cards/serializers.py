from rest_framework import serializers
from .models import MagicCard

class MagicCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagicCard
        fields = ['id', 'name', 'current_value', 'description', 'image_url', 'mana_cost']