from rest_framework import serializers
from .models import HoleScore

class HoleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoleScore
        fields = ('id', 'score',)
