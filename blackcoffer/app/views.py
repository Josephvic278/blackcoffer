from django.shortcuts import render
from .models import *
import json
import time

# Create your views here.
def dashboard(request):
    jd = ""
    with open("/storage/emulated/0/jsondata.json", "r") as d:
        jd = json.load(d)
    
    for get in jd:
        end_year = get["end_year"]
        intensity = get["intensity"]
        sector = get["sector"] 
        topic = get["topic"]
        insight = get["insight"]
        url = get["url"]
        region = get["region"]
        start_year = get["start_year"]
        impact = get["impact"]
        added = get["added"]
        published = get["published"]
        country = get["country"]
        relevance = get["relevance"]
        pestle = get["pestle"]
        title = get["title"]
        likelihood = get["likelihood"]
            
        new_info = Info(end_year = end_year, intensity = intensity,sector = sector, topic = topic, insight = insight, url = url, region = region, start_year = start_year, impact = impact, added = added, published = published, country = country, relevance = relevance, pestle = pestle, title = title,  likelihood = likelihood)
        new_info.save()
        
        print("Saved!!!", print(new_info))
        time.sleep(1)
    print(Info.objects.all())
    return render(request, "dashboard.html")