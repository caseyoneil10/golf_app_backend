from django.db import models

class Holescore(models.Model):
    course = models.CharField(max_length=32)
    hole1 = models.IntegerField()
    hole2 = models.IntegerField()
    hole3 = models.IntegerField()
    hole4 = models.IntegerField()
    hole5 = models.IntegerField()
    hole6 = models.IntegerField()
    hole7 = models.IntegerField()
    hole8 = models.IntegerField()
    hole9 = models.IntegerField()
    hole10 = models.IntegerField()
    hole11 = models.IntegerField()
    hole12 = models.IntegerField()
    hole13 = models.IntegerField()
    hole14 = models.IntegerField()
    hole15 = models.IntegerField()
    hole16 = models.IntegerField()
    hole17 = models.IntegerField()
    hole18 = models.IntegerField()
