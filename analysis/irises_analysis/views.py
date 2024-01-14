from django.shortcuts import render
from django.http import HttpResponse
from . import form_add

# Create your views here.
def index(request):
    return render(request, "irises_analysis/index.html")

def add(request):
    form = form_add.Form_add()
    if request.method == "POST":
        new_iris_form = form_add.Form_add(request.POST)
        if new_iris_form.is_valid():
            data = new_iris_form.cleaned_data
            return HttpResponse(data['sepal_length'])
        else:
            return HttpResponse(new_iris_form)
    return render(request, "irises_analysis/add.html", {'form': form})
