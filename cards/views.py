import csv
import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import MagicCard, CardCollection
from .serializers import MagicCardSerializer, CardCollectionSerializer

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
        
class CardCollectionViewSet(ModelViewSet):
    queryset = CardCollection.objects.all()
    serializer_class = CardCollectionSerializer

@api_view(['POST'])
def bulk_create(request):
    """ 
    Endpoint expects a file in the post body. Currently the file must be
    a csv. Parse the csv and create a new magic card for each row.
    """
    file = request.FILES['file'] 
    decoded_file = file.read().decode('utf-8').splitlines()
    reader = csv.DictReader(decoded_file)
    for row in reader:
        print(row)
    
    return Response({"message": "CSV successfully processed"}, status=201)