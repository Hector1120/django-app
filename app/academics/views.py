from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("::: Welcome to my site :::")

def list_persons(request):
    return HttpResponse("Here you find a list of people")
def create_persons(request):
    return HttpResponse("Create Persons")
