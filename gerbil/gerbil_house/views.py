from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import House
from .forms import AddHouseForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse


def index(request):
    house_list = list(House.objects.all().values().order_by('-house_id'))
    template = loader.get_template('gerbil_house/base.html')

    context = {
        'house_list': house_list,
    }
    return HttpResponse(template.render(context, request))


def add_house_form(request):
    if request.method == "POST":
        form = AddHouseForm(request.POST or None)
        if form.is_valid():
            success_template = loader.get_template('gerbil_house/house_success.html')
            form.save()
            return HttpResponse(success_template.render({}, request))
    else:
        form: AddHouseForm()
    return render(request, 'gerbil_house/house_success.html', {"form": form})


def delete_house_form(request, house_id):
    house = get_object_or_404(House, pk=house_id)
    context = {'house': house}
    success_template = loader.get_template('gerbil_house/base.html')

    if request.method == "GET":
        return render(request, 'gerbil_house/confirm_house_delete.html', context)
    elif request.method == 'POST':
        house.delete()
        messages.success(request, "House has been removed.")
        return render(request, 'gerbil_house/confirm_house_delete.html', context)
    return HttpResponse(success_template.render({}, request))