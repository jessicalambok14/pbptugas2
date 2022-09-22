from django.db import models

class MyWatchList(models.Model):
    watched = models.BooleanField(default=False)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=5)
    release_date = models.CharField(max_length=10)
    review = models.TextField()