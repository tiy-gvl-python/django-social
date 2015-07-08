from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def explain(request):
    return HttpResponse("POTINBBOB: Pictures Of Things I'll Never Build, Buy, Or Bake")