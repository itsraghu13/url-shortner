from django.urls import path
from covid_app.views import covid


# app_name = 'covid_app'


urlpatterns = [
    path('overall-summary/',covid,name="covid")
]
