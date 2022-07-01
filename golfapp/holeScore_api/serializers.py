from rest_framework import serializers
from .models import HoleScore

class HoleScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoleScore
        fields = ('id',
        'course'
        'hole1Score',
        'hole2Score',
        'hole3Score',
        'hole4Score',
        'hole5Score',
        'hole6Score',
        'hole7Score',
        'hole8Score',
        'hole9Score',
        'hole10Score',
        'hole11Score',
        'hole12Score',
        'hole13Score',
        'hole14Score',
        'hole15Score',
        'hole16Score',
        'hole17Score',
        'hole18Score',
        )
