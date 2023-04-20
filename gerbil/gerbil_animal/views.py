import datetime

from django.http import HttpResponse
from django.template import loader
from .models import Gerbil


def index(request):
    gerbil_objects = Gerbil.objects.all().values().order_by('-gerbil_id')
    gerbil_list = list(gerbil_objects)
    gerbil_data = []
    counter = 0
    # for gerbil in gerbil_list:
    #     gerbil_data.append(gerbil['name'])
    template = loader.get_template('gerbil_animal/gerbilpage.html')
    context = {
        'gerbil_list': gerbil_list,
    }
    return HttpResponse(template.render(context, request))


# def gerbil_presentation(request):
#     gerbil_list = Gerbil.objects.values().order_by('name')[:9]
#     for gerbil in gerbil_list:
#         gerbil_name = gerbil.name
#         return gerbil_name
#     a = [gerbil for gerbil in gerbil_list]
#     context = {
#         'gerbil_list': gerbil_list,
#     }
#     template = loader.get_template('gerbil_animal/gerbilpage.html')
#     return HttpResponse(template.render(context, request))
