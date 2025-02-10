from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello seram[pore]")
    return render(request,"websites/index.html")
def about(request):
    return HttpResponse("Hello world you are at about")
def contact(request):
    return HttpResponse("You are at contact")

