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

    Flight_Number = request.GET['Flight_Number']
    OriginAirportID = request.GET['OriginAirportID']
    DestAirportID = request.GET['DestAirportID']
    CRSDepTime = request.GET['CRSDepTime']
    DepTime = request.GET['DepTime']
    TaxiOut = request.GET['TaxiOut']
    WheelsOn = request.GET['WheelsOn']
    TaxiIn = request.GET['TaxiIn']
    CRSArrTime = request.GET['CRSArrTime']
    AirTime = request.GET['AirTime']
    TotalAddGTime = request.GET['TotalAddGTime']

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
    
    classification = result[0]

    return render(request, "results.html", {"result": classification,
                                            "inputParams": inputParams,
                                            "Flight_Number": Flight_Number,
                                            "OriginAirportID": OriginAirportID,
                                            "DestAirportID": DestAirportID,
                                            "CRSDepTime": CRSDepTime,
                                            "DepTime": DepTime,
                                            "TaxiOut": TaxiOut,
                                            "WheelsOn": WheelsOn,
                                            "TaxiIn": TaxiIn,
                                            "CRSArrTime": CRSArrTime,
                                            "AirTime": AirTime,
                                            "TotalAddGTime": TotalAddGTime
                                            })
