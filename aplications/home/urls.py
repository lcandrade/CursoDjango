from django.urls import path
#inportacion de la vista
from . import views


urlpatterns = [
 
    path('', views.IndexView.as_view()),
    path('lista/', views.ListViewPrueba.as_view()),
    path('lista-prueba/', views.ModeloPruebaListView.as_view()),
]
