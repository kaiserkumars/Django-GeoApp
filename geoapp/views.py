from django.shortcuts import render
import requests

def home(request):
    is_cached = ('geodata' in request.session)   #use of request.session to cache results
    if not is_cached:
        ip_address = request.META.get('HTTP_X_FORWARDED_FOR','')
        response = requests.get('https://freegeoip.net/json/%s' % ip_address)
        request.session['geodata'] = response.json() #use of request.session to cache results
        # geodata = response.json()
    # print(geodata['latitude'])
    geodata=request.session['geodata']
    context = {
        'ip':geodata['ip'],
        'country':geodata['country_name'],
        'latitude':geodata['latitude'],
        'longitude':geodata['longitude'],
        'api_key':'AIzaSyBLVOaZ9yIyLhyH_qHqfrNMRkblN-QPYv4',
        'is_cached':is_cached
    }
    return render(request,'geoapp/home.html',context)
# Create your views here.
