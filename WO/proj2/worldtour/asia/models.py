from django.db import models

# Create your models here.


class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_nights = models.IntegerField()
    price = models.IntegerField()
