from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
#    address_line1 = models.CharField(max_length=100)
#    address_city = models.CharField(max_length=100)
#    address_postal_code = models.CharField(max_length=100)
#    address_country = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #total_price = models.FloatField()
    #min_daily_rate = models.FloatField()
    phone_number = models.CharField(max_length=100)
    url = models.CharField(max_length=800)
#    amenities = models.CharField(max_length = 100)