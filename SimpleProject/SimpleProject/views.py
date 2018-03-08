from django.http import HttpResponse

def thanks(request):
    return HttpResponse('thanks')
