from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import MagicCard
from .serializers import MagicCardSerializer

class MagicCardViewSet(ModelViewSet):
    queryset = MagicCard.objects.all()
    serializer_class = MagicCardSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        colors = self.request.query_params.getlist('colors')

        if name:
            return MagicCard.objects.filter(name=name)
        elif colors:
            return MagicCard.objects.filter(mana_cost__contains=colors[0])
        else:
            return MagicCard.objects.all()