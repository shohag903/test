from django.shortcuts import render
from django.http import HttpResponse


def profile(request):
       return render(request,'employee/profile.html')


def employee(request):
       return HttpResponse("this is our page")