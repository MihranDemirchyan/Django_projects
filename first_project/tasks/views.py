from django.shortcuts import HttpResponse
from datetime import datetime


def home_view(request):
    print("request", request)
    return HttpResponse("Hello from django")


def welcome(request):
    print("request", request)
    return HttpResponse(f"Hello, this is my web page, {datetime.now().time()}")


