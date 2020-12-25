from django.shortcuts import render
from django.http import HttpResponse
from .models import MyUrl
# Create your views here.
def index(request):
    return HttpResponse(" xin chao he thong")
    
def display(request):
    my_url=MyUrl.objects.all()
    template = '<a href="{url}">{alias}</a> --> {url}<br/>'
    value=''
    for url in my_url:
        value += template.format(alias=url.alias, url=url.url)
    return HttpResponse(value)

