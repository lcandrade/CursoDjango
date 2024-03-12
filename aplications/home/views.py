from django.shortcuts import render
from django.views.generic import TemplateView, ListView

# Create your views here.
from .models import Prueba


class IndexView(TemplateView):
    template_name = 'home/home.html'

class ListViewPrueba(ListView):    
    template_name= 'home/list.html'
    queryset=['a', 'b', 'c']
    context_object_name='lista_prueba'

class ModeloPruebaListView(ListView):
    model=Prueba
    template_name= "home/pruebas.html"
    context_object_name= "Lista_prueba"
