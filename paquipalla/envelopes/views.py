from django.shortcuts import render

# Create your views here.

def mainpage(request):
    return HttpResponse("<html><body>HELLO</body></html>")
