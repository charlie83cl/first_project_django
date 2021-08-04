from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Mensaje Mensaje Mensaje")

def root(request):
    return redirect("/blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un formu. para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, escribe_un_valor):
    return HttpResponse(f"en este mensaje se une tu numero consultado +{escribe_un_valor}")

def edit(request, escribe_un_valor):
    return HttpResponse(f"solicitud de edicion de blog numero +{escribe_un_valor}, hagalo con responsabilidad")

def carta(request, escribe_un_texto):
    return HttpResponse(f"en este mensaje se une este mensaje con lo que escribas en la carta ++++++{escribe_un_texto}")

def destroy(request, escribe_un_valor):
    return redirect("/")

def json(request):
    return JsonResponse({
        'tittle':'letrerito para mostrar titulos json', 
        'name': 'Charlie',
        'curso': 'FullStack Python'
    })

