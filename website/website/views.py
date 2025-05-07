from django.http import HttpResponse
from django.conf.urls import include
from django.shortcuts import render

def welcome(request):
    return render(request,'index.html')

# def about(request):
#     return render(request,include('about.urls'))

def contact(request):
    return render(request, 'kontak.html')