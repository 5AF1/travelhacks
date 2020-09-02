from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) ###(auto_now_add = True) (auto_now = True) kora jay ete
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={'pk':self.pk})

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

