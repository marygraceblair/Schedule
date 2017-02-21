from django.http import HttpResponse

def home(request):
    html = "Hello World"
    return HttpResponse(html)
