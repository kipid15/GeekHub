from django.shortcuts import render
from .models import Data

# Create your views here.
def index(request):
    return render(request, 'mainPage/home.html')

def thanks(request):
    datas = Data.objects.all().order_by('submitTime')
    return render(request, 'mainPage/thanks.html', {'datas': datas})
