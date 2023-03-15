from django.shortcuts import render
from django.http import HttpResponse
# from gerbil.gerbil_animal.models import Gerbil


def intro(request, id):
    return HttpResponse(f"Here is your Specific Gerbil {id}")
