
import os
import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    times = int(os.environ.get('TIMES', 3))
    r = requests.get('https://httpbin.org/status/418')
    print(r.text)
    return HttpResponse(('<pre>' + r.text + '</pre>') * times )

# combined them both above for TWO teapots yeeyee
# def index(request):
#     times = int(os.environ.get('TIMES', 3))
#     return HttpResponse('Hello! ' * times)

"""
after generating first table via: heroku run python manage.py migrate
Now you can access the https://beginner-python.herokuapp.com/db/ route again,
and you’ll see a simple page update every time you access it:

The code to access the database is straightforward,
and makes use of a simple Django model called Greetings
that you can find in hello/models.py.

Whenever you visit the /db route of your app,
the following method in the hello/views.py file is invoked
which creates a new Greeting and then renders all the existing Greetings:
"""
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
