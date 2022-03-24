from django.shortcuts import render
from django.http import HttpResponse
def first_view(request):
    s='<h1> first view information </h1>'
    return HttpResponse(s)
def second_view(request):
    s='<h1> second view information </h1>'
    return HttpResponse(s)
def third_view(request):
    s='<h1> third view information </h1>'
    return HttpResponse(s)
