from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Cage



def index(request):
    cage_objects = Cage.objects.all().values().order_by('-cage_id')
    template = loader.get_template('gerbil_cage/base.html')

    context = {
        'cage_objects': cage_objects,
    }
    return HttpResponse(template.render(context, request))
