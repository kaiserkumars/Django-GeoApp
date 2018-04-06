from django.shortcuts import render
import requests

def home(request):
    ip_address = request.META.get('HTTP_X_FORWARDED_FOR','')
    response = requests.get('https://freegeoip.net/json/%s' % ip_address)
    geodata = response.json()
    context = {
        'ip':geodata['ip'],
        'country':geodata['country_name'],
        'latitude':geodata['latitude'],
        'longitude':geodata['longitude'],
        'api_key':'AIzaSyBLVOaZ9yIyLhyH_qHqfrNMRkblN-QPYv4'
    }
    return render(request,'geoapp/home.html',context)
# Create your views here.
