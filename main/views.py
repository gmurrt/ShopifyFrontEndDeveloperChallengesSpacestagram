from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
import requests
import json
from main.models import Like

def index(request):
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key='+settings.NASA_API_KEY)
    loaded_json = json.loads(response.text)

    daily_image = loaded_json.get('url')
    title = loaded_json.get('title')
    explanation = loaded_json.get('explanation')
    date = loaded_json.get('date')
    owner = loaded_json.get('copyright')

    context = {
        'daily_image': daily_image,
        'title':title,
        'explanation':explanation,
        'date':date,
        'owner':owner,
        'liked': Like
    }
    return render(request, 'main/main.html', context)
    
def loading(request):
    return render(request, 'main/index.html')
    