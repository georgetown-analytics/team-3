from django.db import models

# Create your models here.

class Flight(models.Model):
    FlightDate = models.DateTimeField(auto_now_add=True),
    Operating_Airline = models.CharField(max_length=255),
    Tail_Number = models.CharField(max_length=255),
    Flight_Number = models.CharField(max_length=255),
    OriginAirportID = models.CharField(max_length=255),
    DestAirportID = models.CharField(max_length=255),
    CRSDepTime = models.CharField(max_length=255),
    DepTime = models.CharField(max_length=255),
    DepDelay = models.CharField(max_length=255),
    DepDel15 = models.CharField(max_length=255),
    DepDelayMinutes = models.CharField(max_length=255),
    DepTimeBlk = models.CharField(max_length=255),
    TaxiOut = models.CharField(max_length=255),
    WheelsOn = models.CharField(max_length=255),
    TaxiIn = models.CharField(max_length=255),
    CRSElapsedTime = models.CharField(max_length=255),
    AirTime = models.CharField(max_length=255),
    Distance = models.CharField(max_length=255),
    latitude = models.CharField(max_length=255),
    longitude = models.CharField(max_length=255),
    DepDelayClass = models.CharField(max_length=255),
    
