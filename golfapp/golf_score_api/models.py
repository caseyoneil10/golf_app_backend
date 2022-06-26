from django.db import models

# Create your models here.

class Score(models.Model):
    date = models.CharField(max_length=32)
    course = models.CharField(max_length=50)
    score = models.IntegerField()
    weather = models.CharField(max_length=32)
