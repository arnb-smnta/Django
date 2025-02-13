from django.shortcuts import render, get_object_or_404
from .models import ChaiVariety, store
from .forms import ChaiVarietyForm
# Create your views here.


def all_chai(request):
    chais = ChaiVariety.objects.all()
    return render(request, "chai/all_chai.html", {"chais": chais})


def chaiDetails(request, chaiId):
    chai = get_object_or_404(ChaiVariety, pk=chaiId)
    return render(request, "chai/chai_details.html", {"chaiDetails": chai})


def chai_store_view(request):
    stores = None
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data["chai_variety"]
            stores = store.objects.filter(ChaiVariety=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, "chai/chai_stores.html", {"stores": stores, "form": form})
