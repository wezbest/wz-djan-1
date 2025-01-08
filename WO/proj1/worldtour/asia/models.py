from django.db import models

# Create your models here.


class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_nights = models.IntegerField()
    price = models.IntegerField()

    # String representation of the tours
    def __str__(self):
        return f"ID:{self.id}, Origin: {self.origin_country}, Destination: {self.destination_country}, Nights: {self.number_nights}, Price: ${self.price}"
