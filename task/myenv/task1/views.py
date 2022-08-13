from tkinter.font import names
from unicodedata import name
from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.name 
names=['hassan','Ali','mohammad']
def task1(reguest):

    
    return render(reguest,'task1/index.html',{
        'names':names
    })