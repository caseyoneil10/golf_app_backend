from django.shortcuts import render

from rest_framework import generics
from .serializers import ScoreSerializer
from .models import Score

class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all().order_by('id') #
    serializer_class = ScoreSerializer # tell django what serializer to use

class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all().order_by('id')
    serializer_class = ScoreSerializer
