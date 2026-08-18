from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1 style='color:red;'>Hello Home</h1>") 
def about_us(request):
    return HttpResponse("<h1 style='color:red;'>Hello About_us</h1>") 