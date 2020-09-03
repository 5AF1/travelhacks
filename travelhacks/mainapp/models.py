from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) ###(auto_now_add = True) (auto_now = True) kora jay ete
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ###'''###
    image1 = models.ImageField(default='default.jpg', upload_to='post_pics')
    image2 = models.ImageField(default='default.jpg', upload_to='post_pics')
    #ss = content[0]
    ###'''###

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        img1 = Image.open(self.image1.path)
        if img1.height > 300 or img1.width > 600:
            output_size = (600, 300)
            img1.thumbnail(output_size)
            img1.save(self.image1.path)
        img2 = Image.open(self.image2.path)
        if img2.height > 300 or img2.width > 600:
            output_size = (600, 300)
            img2.thumbnail(output_size)
            img2.save(self.image2.path)

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

