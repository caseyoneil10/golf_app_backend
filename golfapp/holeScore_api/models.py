from django.db import models


class HoleScore(models.Model):
    date = models.CharField(max_length=64)
    hole1Score = models.IntegerField()
    hole2Score = models.IntegerField()
    hole3Score = models.IntegerField()
    hole4Score = models.IntegerField()
    hole5Score = models.IntegerField()
    hole6Score = models.IntegerField()
    hole7Score = models.IntegerField()
    hole8Score = models.IntegerField()
    hole9Score = models.IntegerField()
    hole10Score = models.IntegerField()
    hole11Score = models.IntegerField()
    hole12Score = models.IntegerField()
    hole13Score = models.IntegerField()
    hole14Score = models.IntegerField()
    hole15Score = models.IntegerField()
    hole16Score = models.IntegerField()
    hole17Score = models.IntegerField()
    hole18Score = models.IntegerField()
