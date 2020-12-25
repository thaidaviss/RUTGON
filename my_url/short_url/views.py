from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUrl
# Create your views here.
def index(request):
    return HttpResponse(" xin chao he thong")
    
def display(request):
    my_url=MyUrl.objects.all()
    template=

