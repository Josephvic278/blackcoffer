from django.shortcuts import render
from .models import *
import json
import time

# Create your views here.
def dashboard(request):
    model_data =  Info.objects.all()
    return render(request, "dashboard.html", {'data':model_data})