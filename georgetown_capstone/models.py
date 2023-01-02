from django.db import models

# Create your models here.

class PredictionResult(models.Model):
    Flight_Number = models.FloatField()
    OriginAirportID = models.FloatField()
    DestAirportID = models.FloatField()
    CRSDepTime = models.FloatField()
    DepTime = models.FloatField()
    TaxiOut = models.FloatField()
    WheelsOn = models.FloatField()
    TaxiIn = models.FloatField()
    CRSArrTime = models.FloatField()
    AirTime = models.FloatField()
    TotalAddGTime = models.FloatField()
    classification = models.FloatField()
    
def __float__(self):
    return self.classification 
    
    
    
