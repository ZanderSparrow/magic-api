from rest_framework import serializers
from .models import MagicCard, CardCollection

class MagicCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagicCard
        fields = ['id', 'name', 'current_value', 'description', 'image_url', 'mana_cost', 'set_name']


class CardCollectionSerializer(serializers.ModelSerializer):
    cards = MagicCardSerializer(read_only=True, many=True)

    class Meta:
        model = CardCollection
        fields = ['id', 'name', 'description', 'cards']
