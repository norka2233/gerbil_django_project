from django.http import HttpResponse
from django.template import loader

from .models import Gerbil


def index(request):
    gerbil_list = Gerbil.objects.order_by('name')[:9]
    a = ''.join([gerbil.name for gerbil in gerbil_list])
    context = {
        'gerbil_list': gerbil_list,
    }
    template = loader.get_template('gerbil_animal/homepage.html')
    return HttpResponse(template.render(context, request))


def gerbil_presentation(request, gerbil_id):
    return HttpResponse(f"Here is your gerbil {gerbil_id}")