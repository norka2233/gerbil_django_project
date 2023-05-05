from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import House
from .forms import AddHouseForm
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


def delete_house(request, id):
    if request.method == "POST":
        house_list = House.objects.all().get(id=id)
        house_list.delete()
    else:
        house_list: AddHouseForm()
    # return HttpResponseRedirect(reverse('index'))
    return render(request, 'gerbil_house/base.html', {"house_list": house_list})
