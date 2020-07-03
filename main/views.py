from django.shortcuts import render
from django.http import HttpResponse
from .models import Availability
# Create your views here.


def index(request):
    availabilities = Availability.objects.all()
    return render(request, 'index.html', {'availabilities': availabilities})
