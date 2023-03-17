from django.http import HttpResponse
from django.template import loader
from .models import Gerbil


def index(request, id):
    gerbil_list = Gerbil.objects.filter(id=id)
    template = loader.get_template('gerbil_specific/base.html')
    context = {
        'gerbil_list': gerbil_list,
    }
    return HttpResponse(template.render(context, request))


# def gerbil_presentation(request):
#     gerbil_list = Gerbil.objects.values().order_by('name')[:9]
#     a = [gerbil for gerbil in gerbil_list]
#     context = {
#         'gerbil_list': gerbil_list,
#     }
#     template = loader.get_template('gerbil_specific/base.html')
#     return HttpResponse(template.render(context, request))
