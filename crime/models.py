from django.db import models

# Create your models here.
class Crime(models.Model):
    type = models.CharField(max_length=100)
    datetime = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
