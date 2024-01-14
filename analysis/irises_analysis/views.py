from django.shortcuts import render
from django.http import HttpResponse
from . import form_add

# Create your views here.
def index(request):
    return render(request, "irises_analysis/index.html")

def add(request):
    form = form_add.Form_add()
    return render(request, "irises_analysis/add.html", {'form': form})
