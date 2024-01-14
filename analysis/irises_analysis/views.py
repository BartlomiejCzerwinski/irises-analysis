from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
import requests
from . import form_add
from . import models

# Create your views here.
def index(request):
    api_get_data_url = 'http://127.0.0.1:8000/api/data'
    response = requests.get(api_get_data_url)
    if response.status_code == 200:
        data = response.json()
        print(data)
        return render(request, "irises_analysis/index.html", {'data': data})
    return render(request, "irises_analysis/index.html")

def add(request):
    form = form_add.Form_add()
    if request.method == "POST":
        new_iris_form = form_add.Form_add(request.POST)
        if new_iris_form.is_valid():
            data = new_iris_form.cleaned_data
            iris = models.Iris(sepal_length=data["sepal_length"],
                                sepal_width=data["sepal_width"],
                                petal_length=data["petal_length"],
                                petal_width=data["petal_width"],
                                iris_class=data["iris_class"])
            iris.save()
            return HttpResponse(data['iris_class'])
        else:
            return HttpResponse(new_iris_form)
    return render(request, "irises_analysis/add.html", {'form': form})

def data(request):
    if request.method == "GET":
        queryset = models.Iris.objects.all()
        data = serialize('json', queryset)
        return HttpResponse(data)
    if request.method == "POST":
        return HttpResponse("POST")
