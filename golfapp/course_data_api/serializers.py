from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
        'name',
        'totalYards',
        'slopeRating',
        'courseRating',
        'hole1Yardage',
        'hole1Par',
        'hole2Yardage',
        'hole2Par',
        'hole3Yardage',
        'hole3Par',
        'hole4Yardage',
        'hole4Par',
        'hole5Yardage',
        'hole5Par',
        'hole6Yardage',
        'hole6Par',
        'hole7Yardage',
        'hole7Par',
        'hole8Yardage',
        'hole8Par',
        'hole9Yardage',
        'hole9Par',
        'hole10Yardage',
        'hole10Par',
        'hole11Yardage',
        'hole11Par',
        'hole12Yardage',
        'hole12Par',
        'hole13Yardage',
        'hole13Par',
        'hole14Yardage',
        'hole14Par',
        'hole15Yardage',
        'hole15Par',
        'hole16Yardage',
        'hole16Par',
        'hole17Yardage',
        'hole17Par',
        'hole18Yardage',
        'hole18Par',  )