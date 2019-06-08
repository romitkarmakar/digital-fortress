from django.http import HttpResponse

def getHints(request):
    return HttpResponse("Hints")