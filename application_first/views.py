from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to python django project")

def about(request):
    return HttpResponse("Welcome to about page")

