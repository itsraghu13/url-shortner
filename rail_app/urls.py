from django.urls import path
from rail_app.views import pnr_check

urlpatterns = [
    path('pnr-check/',pnr_check,name="pnr_check")
]
