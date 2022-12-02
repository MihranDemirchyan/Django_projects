from django.shortcuts import HttpResponse
from datetime import datetime


def greeting(request):
    return HttpResponse("Greetings to all!!")


def introduction(request):
    return HttpResponse("This has created for greetings, current date and time, and for task about dictionaries.")


def current_time(request):
    return HttpResponse(f"This is current time and date {datetime.now()}")


def dictionary_keys_squares(request) -> HttpResponse:
    """This function returns dictionary which values are the keys squares"""

    dict_ = {}

    for i in range(1, 16):
        dict_[i] = i**2
    return HttpResponse(f"And finally here is our dictionary {dict_}")
