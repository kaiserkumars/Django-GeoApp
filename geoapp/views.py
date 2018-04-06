from django.shortcuts import render
import requests

def home(request):
    response = requests.get('https://freegeoip.net/json')
    geodata = response.json()
    context = {
        'ip':geodata['ip'],
        'country':geodata['country_name']
    }
    return render(request,'geoapp/home.html',context)
# Create your views here.
