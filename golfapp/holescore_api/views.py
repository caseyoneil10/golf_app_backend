from django.shortcuts import render

from rest_framework import generics
from .serializers import HolescoreSerializer
from .models import Holescore

class HolescoreList(generics.ListCreateAPIView):
    queryset = Holescore.objects.all().order_by('id')
    serializer_class = HolescoreSerializer

class HolescoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holescore.objects.all().order_by('id')
    serializer_class = HolescoreSerializer
