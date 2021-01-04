
from django.contrib.auth.decorators import login_required
from django.http import response
from django.shortcuts import render
import requests

# Create your views here.
@login_required(login_url='/login/')
def covid(request):
    url = 'https://api.covid19api.com/summary'
    response = requests.get(url,verify=False)
    result = response.json()
    global_data = result['Global']
    countries_data = result['Countries']
    

    context = {
        'global_data' : global_data,
        'countries_data' : countries_data
    }

    return render(request,'covid.html',context)