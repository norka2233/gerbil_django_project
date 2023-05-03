import datetime

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .models import Gerbil
from django.views.decorators.csrf import csrf_protect
from django.views import generic
from django.shortcuts import get_object_or_404

from .forms import AddGerbilForm


def index(request):
    gerbil_list = list(Gerbil.objects.all().values().order_by('-gerbil_id'))
    template = loader.get_template('gerbil_animal/gerbilpage.html')
    context = {
        'gerbil_list': gerbil_list,
    }
    return HttpResponse(template.render(context, request))


# @csrf_protect
def add_gerbil_form(request):
    if request.method == "POST":
        form = AddGerbilForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gerbil/success')
    else:
        form = AddGerbilForm()

    return render(request, 'gerbil_animal/success.html', {"form": form})


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
