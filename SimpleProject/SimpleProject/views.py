from django.http import HttpResponse
from django.shortcuts import render

def thanks(request):
    return HttpResponse('thanks')

def dataGrid(request):
    return(render(request, 'mainPage/dataGrid.html'))