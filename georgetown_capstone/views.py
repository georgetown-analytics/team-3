from django.shortcuts import render
from django.http import HttpResponse

# request handler
def home(request):
    return render(request,"index.html", {"title": "Cohort 28 Capstone Project"})
