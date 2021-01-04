from django.shortcuts import render

# Create your views here.
def pnr_check(request):
    return render(request,'pnrcheck.html')