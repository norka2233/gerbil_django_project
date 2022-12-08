import os
base = os.path.abspath('gerbil/templates')

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('gerbil_animal/index.html')
    return HttpResponse(template.render())


def gerbil_presentation(request, gerbil_id):
    return HttpResponse(f"Here is your gerbil {gerbil_id}")