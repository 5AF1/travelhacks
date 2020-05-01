from django.db import models

# Create your models here.

class Tour(models.Model):
    name = models.CharField(max_length=25)
    season = models.CharField(max_length=25)
    guide = models.CharField(max_length=25)
    cost = models.DecimalField(decimal_places = 2,max_digits=10,default=0)

    def __str__(self):
        return self.name


class Spot(models.Model):
    onTour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    visited = models.BooleanField()

    def __str__(self):
        return self.name

