from django.db import models

# Create your models here.

class Flight(models.Model):
    Flight_Number = models.FloatField(max_length=255),
    OriginAirportID = models.FloatField(max_length=255),
    DestAirportID = models.FloatField(max_length=255),
    CRSDepTime = models.FloatField(max_length=255),
    DepTime = models.FloatField(max_length=255),
    TaxiOut = models.FloatField(max_length=255),
    WheelsOn = models.FloatField(max_length=255),
    TaxiIn = models.FloatField(max_length=255),
    CRSArrTime = models.FloatField(max_length=255),
    AirTime = models.FloatField(max_length=255),
    TotalAddGTime = models.FloatField(max_length=255),
    
