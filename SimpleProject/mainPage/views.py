from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'mainPage/home.html')

def thanks(request):
    return render(request, 'mainPage/thanks.html')