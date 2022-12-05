from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hey, here is your gerbil!")


def gerbil_presentation(request, gerbil_id):
    return HttpResponse(f"Here is your gerbil {gerbil_id}")