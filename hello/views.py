import os

from django.shortcuts import render
from django.http import HttpResponse
import requests

from .models import Greeting

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES', 3))
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    return HttpResponse('Hello user! ' * times)



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
