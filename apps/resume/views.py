from django.shortcuts import render,redirect
from django.http import HttpResponse 

# Create your views here.

# Landing Page
def index(request):
    return render(request,'index.html')
