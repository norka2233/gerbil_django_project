from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
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
    context = {'gerbil_list': gerbil_list}
    return HttpResponse(template.render(context, request))


def add_gerbil_form(request):
    if request.method == "POST":
        form = AddGerbilForm(request.POST)
        if form.is_valid():
            success_template = loader.get_template('gerbil_animal/gerbil_success.html')
            form.save()
            return HttpResponse(success_template.render({}, request))
    else:
        form = AddGerbilForm()
    return render(request, 'gerbil_animal/gerbil_success.html', {"form": form})


def delete_gerbil_form(request, gerbil_id):
    gerbil = get_object_or_404(Gerbil, pk=gerbil_id)
    context = {'gerbil': gerbil}
    success_template = loader.get_template('gerbil_animal/gerbilpage.html')

    if request.method == 'GET':
        return render(request, 'gerbil_animal/confirm_gerbil_delete.html', context)
    elif request.method == 'POST':
        gerbil.delete()
        messages.success(request, "Gerbil has been removed.")
        return render(request, 'gerbil_animal/confirm_gerbil_delete.html', context)
    return HttpResponse(success_template.render({}, request))



