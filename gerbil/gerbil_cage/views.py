from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cage


def index(request):
    gerbil_cage = Cage.objects.values()
    a = [gerbil for gerbil in gerbil_cage]
    context = {
        'gerbil_cage': gerbil_cage,
    }
    template = loader.get_template('gerbil_cage/base.html')
    return HttpResponse(template.render(context, request))
