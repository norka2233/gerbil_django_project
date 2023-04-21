from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import House


def index(request):
    house_objects = House.objects.all().values()
    house_list = list(house_objects)
    template = loader.get_template('gerbil_house/base.html')
    context = {
        'gerbil_house': house_objects,
    }
    return HttpResponse(template.render(context, request))