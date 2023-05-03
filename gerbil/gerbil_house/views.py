from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import House
from .forms import AddHouseForm


def index(request):
    house_list = list(House.objects.all().values())
    template = loader.get_template('gerbil_house/base.html')

    context = {
        'house_list': house_list,
    }
    return HttpResponse(template.render(context, request))


def add_house_form(request):
    if request.method == "POST":
        form = AddHouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form: AddHouseForm()
    return render(request, 'gerbil_house/success.html', {"form": form})