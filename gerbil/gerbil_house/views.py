from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import House


def index(request):
    gerbil_house = House.objects.values()
    a = [house for house in gerbil_house]
    context = {
        'gerbil_house': gerbil_house,
    }
    template = loader.get_template('gerbil_house/base.html')
    return HttpResponse(template.render(context, request))