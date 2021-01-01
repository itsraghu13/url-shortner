from django.shortcuts import redirect, render
from .models import City
import requests


def weather(request):
    # Api_key = "b803cfd77873c48f887c11f0f1d5c83f"
    # url = "http://api.openweathermap.org/data/2.5/weather?"
    

    # if request.method == "POST":
    #     if request.POST['city']:
                
    #         create_city = City(name=request.POST['city'])
    #         create_city.save()
    #         if request.POST['next'] != '':
    #             return redirect(request.POST.get('next'))
    #         else:
    #             return redirect('weather')
    #     return render(request, 'weather.html')

    # cities = City.objects.all()
    # weather_data = []

    # for city in cities:
    #     complete_url = url + "appid=" + Api_key + "&q=" + str(city)
    #     print(complete_url)

    #     r = requests.get(complete_url).json()

    #     city_weather = {
    #         'city': city.name,
    #         'temperature' : r['main']['temp'],
    #         'description' : r['weather'][0]['description'],
    #         'icon' : r['weather'][0]['icon'],
    #     }

    #     weather_data.append(city_weather)

    # context = {
    #     'weather_data' : weather_data, 
    #     }

    return render(request,'weather.html')