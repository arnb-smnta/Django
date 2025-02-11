from django.shortcuts import render,get_object_or_404
from .models import ChaiVariety
# Create your views here.


def all_chai(request):
    chais=ChaiVariety.objects.all
    return render(request,'chai/all_chai.html',{'chais':chais})
def chaiDetails(request,chaiId):
    chai= get_object_or_404(ChaiVariety,pk=chaiId)
    return render(request,'chai/chai_details.html',{'chaiDetails':chai})