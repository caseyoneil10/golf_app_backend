from django.shortcuts import render

from rest_framework import generics
from .serializers import HoleScoreSerializer
from .models import Holescore

class HoleScoreList(generics.ListCreateAPIView):
    queryset = Holescore.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = HoleScoreSerializer # tell django what serializer to use

class HoleScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holescore.objects.all().order_by('id')
    serializer_class = HoleScoreSerializer
