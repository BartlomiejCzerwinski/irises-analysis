from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.serializers import serialize
import requests
import json
from . import form_add
from . import models
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def index(request):
    api_get_data_url = 'http://127.0.0.1:8000/api/data'
    response = requests.get(api_get_data_url)
    if response.status_code == 200:
        data = response.json()
        return render(request, "irises_analysis/index.html", {'data': data})
    return render(request, "irises_analysis/index.html")

def add(request):
    api_add_data_url = 'http://127.0.0.1:8000/api/data'
    form = form_add.Form_add()
    if request.method == "POST":
        csrf_token = get_token(request)
        csrf_cookie = {'csrftoken': csrf_token}
        cookies = requests.utils.cookiejar_from_dict(csrf_cookie)
        response = requests.post(api_add_data_url, data=request.POST, cookies = cookies)
        if response.status_code == 200:
            return redirect('index')
        elif response.status_code == 400:
            return HttpResponse("400 error")
    return render(request, "irises_analysis/add.html", {'form': form})

def predict(request):
    form = form_add.Form_predict()
    if request.method == "POST":
        sepal_length = request.POST['sepal_length']
        sepal_width = request.POST['sepal_width']
        petal_length = request.POST['petal_length']
        petal_width = request.POST['petal_width']

        api_predict_url = 'http://127.0.0.1:8000/api/predictions' + \
                            "?sepal_length=" + sepal_length + \
                            "&sepal_width=" + str(sepal_width) + \
                            "&petal_length=" + str(petal_length) + \
                            "&petal_width=" + str(petal_width)

        csrf_token = get_token(request)
        csrf_cookie = {'csrftoken': csrf_token}
        cookies = requests.utils.cookiejar_from_dict(csrf_cookie)
        headers = {'X-CSRFToken': csrf_token}
        response = requests.post(api_predict_url, cookies=cookies, headers=headers)

    return render(request, "irises_analysis/predict.html", {'form': form})

def api_predictions(request):
    print("REQUEST:", str(request))
    sepal_length = request.GET.get('sepal_length')
    sepal_width = request.GET.get('sepal_width')
    petal_length = request.GET.get('petal_length')
    petal_width = request.GET.get('petal_width')
    form = form_add.Form_predict({
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        })
    if form.is_valid():
        pass
    else:
        message = {"message": "Invalid data"}
        json_message = json.dumps(message)
        return HttpResponse(json_message, status=400)

def generate_plot():
    x = [4, 5, 10, 4, 3, 11, 14 , 8, 10, 12]
    y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    z = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
    classes = [0, 0, 1, 0, 0, 1, 1, 0, 1, 1]

    plt.scatter(x, y, s=z, c=classes)

    buffer = BytesIO()
    plt.savefig(buffer, format="jpg")
    buffer.seek(0)

    img_jpg = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(img_jpg).decode('utf-8')
    return graphic


def api_data(request):
    if request.method == "GET":
        queryset = models.Iris.objects.all()
        data = serialize('json', queryset)
        return HttpResponse(data, content_type='application/json')
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
            iris_json = serialize('json', [iris])
            return JsonResponse(iris_json, safe=False)
        else:
            message = {"message": "Invalid data"}
            json_message = json.dumps(message)
            return HttpResponse(json_message, status=400)

@require_http_methods(["POST"])
def delete(request, record_id):
    if request.method == "POST":
        csrf_token = get_token(request)
        csrf_cookie = {'csrftoken': csrf_token}
        headers = {'X-CSRFToken': csrf_token}
        cookies = requests.utils.cookiejar_from_dict(csrf_cookie)
        api_delete_data_url = 'http://127.0.0.1:8000/api/data/' + record_id
        response = requests.delete(api_delete_data_url, headers=headers, cookies=cookies)
        if response.status_code == 200:
            return redirect("/", status=200)
        else:
            return HttpResponse("404 error", status=404)

def api_delete(request, record_id):
    if request.method == "DELETE":
        try:
            iris = models.Iris.objects.get(id=record_id)
            iris.delete()
            return HttpResponse({"deleted_id": record_id}, status=200)
        except:
            return HttpResponse({"error": "Record not found"}, status=404)
