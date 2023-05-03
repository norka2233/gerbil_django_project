from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Cage
from .forms import AddCageForm


def index(request):
    cage_list = list(Cage.objects.all().values().order_by('-cage_id'))
    template = loader.get_template('gerbil_cage/base.html')

    context = {
        'cage_objects': cage_list,
    }
    return HttpResponse(template.render(context, request))


def add_cage_form(request):
    if request.method == "POST":
        form = AddCageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form: AddCageForm()
    return render(request, 'gerbil_cage/success.html', {"form": form})
