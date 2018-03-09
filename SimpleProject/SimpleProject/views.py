from django.shortcuts import render

def thanks(request):
    return render(request, 'mainPage/thanks.html')

def dataGrid(request):
    return(render(request, 'mainPage/dataGrid.html'))