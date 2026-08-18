from django.shortcuts import render
from django.http import HttpResponse

def mypage(request):
    return HttpResponse("<h1 style='color:red;'>New Career mypage</h1>") 