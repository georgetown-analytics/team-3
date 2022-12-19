from django.shortcuts import render
from django.http import HttpResponse
import joblib

# request handler

model_pkl = "flight-adaboost-classifier.pickle"

def home(request):
    return render(request, "predict.html", {"title": "Cohort 28 Capstone Project"})


def results(request):
    model = joblib.load(model_pkl)

    inputParams = []

    inputParams.append(request.GET['Flight_Number'])
    inputParams.append(request.GET['OriginAirportID'])
    inputParams.append(request.GET['DestAirportID'])
    inputParams.append(request.GET['CRSDepTime'])
    inputParams.append(request.GET['DepTime'])
    inputParams.append(request.GET['TaxiOut'])
    inputParams.append(request.GET['WheelsOn'])
    inputParams.append(request.GET['TaxiIn'])
    inputParams.append(request.GET['CRSArrTime'])
    inputParams.append(request.GET['AirTime'])
    inputParams.append(request.GET['TotalAddGTime'])

    result = model.predict([inputParams])

    return render(request, "results.html", {"result": result,"inputParams": inputParams})

                 
              





