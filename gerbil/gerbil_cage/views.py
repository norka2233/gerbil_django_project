from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import Cage
from .forms import AddCageForm
from django.shortcuts import get_object_or_404
from django.contrib import messages



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
            success_template = loader.get_template('gerbil_cage/cage_success.html')
            form.save()
            return HttpResponse(success_template.render({}, request))
    else:
        form: AddCageForm()
    return render(request, 'gerbil_cage/cage_success.html', {"form": form})


def delete_cage_form(request, cage_id):
    cage = get_object_or_404(Cage, pk=cage_id)
    context = {'cage': cage}
    success_template = loader.get_template('gerbil_cage/base.html')

    if request.method == 'GET':
        return render(request, 'gerbil_cage/confirm_cage_delete.html', context)
    elif request.method == 'POST':
        cage.delete()
        messages.success(request, 'Cage has been removed. ')
        return render(request, 'gerbil_cage/confirm_cage_delete.html', context)
    return HttpResponse(success_template.render({}, request))
