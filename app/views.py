from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def jampandu(request):
    return HttpResponse("<h1><marquee> HI JIGELRANI HOW ARE YOU</h1></marquee>")

def jigelrani(request):
    return HttpResponse("<h1><marquee> HI JAMPANDU IAM FINE</h1></marquee>")
