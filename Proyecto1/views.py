from django.shortcuts import render
from django.http import HttpResponse

def index (request):    
    suma= 5+5
    return render (request, 'index.html', {
        #context
        'title':'Curso Django',
        'message':'Curos de Django 2024',
        'products': [
             {'title':'Camisa', 'price':50, 'stock':True},
             {'title':'Pantalon', 'price':100, 'stock':False},
             {'title':'Gafas', 'price':35, 'stock':True}
         ]
    })
