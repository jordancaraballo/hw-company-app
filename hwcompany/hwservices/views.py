from django.shortcuts import render, render_to_response
from django.contrib import admin
from hwservices.models import Manufacturer as manufacturer

# Create your views here.
def index(request):
    return render_to_response('index.html')

def manufacturers(request):
    istekler = manufacturer.objects.all()
    return render(request, 'list.html', locals())

# In progress
def manufacturersStates(request):
    istekler = manufacturer.objects.all()
    return render(request, 'list.html', locals())

# Ideas
# Reporte uno - listar todas las companias con sus numeros de cuenta y localidad
# Reporte dos - listar 
