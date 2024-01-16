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
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

IRIS_CLASSES = {'1': 'Setosa',
                '2': 'Versicolour',
                '3': 'Virginica'}


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
        if response.status_code == 200:
            response_str = response.content.decode('utf-8')
            response_dict = json.loads(response_str)
            predicted_class = response_dict["class"]
            print("MY RESPONSE: ", str(response_str))
            generate_pair_plots()
            return render(request, "irises_analysis/predicted.html", {'class': IRIS_CLASSES[predicted_class]})
        else:
            return HttpResponse("400 error")

    return render(request, "irises_analysis/predict.html", {'form': form})

def generate_pair_plots():
    iris_data = models.Iris.objects.all().values()
    iris_df = pd.DataFrame.from_records(iris_data)
    plt.scatter(iris_df["sepal_length"], iris_df["sepal_width"], c=iris_df["iris_class"])
    plt.show()
    print(iris_df)

def api_predictions(request):
    print("REQUEST:", str(request))
    sepal_length = float(request.GET.get('sepal_length'))
    sepal_width = float(request.GET.get('sepal_width'))
    petal_length = float(request.GET.get('petal_length'))
    petal_width = float(request.GET.get('petal_width'))
    form = form_add.Form_predict({
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        })
    if form.is_valid():
        all_instances = models.Iris.objects.values_list('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        labels = models.Iris.objects.values_list('iris_class', flat=True)
        knn_model = KNeighborsClassifier(n_neighbors=3)
        knn_model.fit(all_instances, labels)
        test_instance = [[sepal_length, sepal_width, petal_length, petal_width]]
        predicted_class = knn_model.predict(test_instance)
        message = {"class": str(predicted_class[0])}
        json_message = json.dumps(message)
        return HttpResponse(json_message, status=200)
    else:
        message = {"message": "Invalid data"}
        json_message = json.dumps(message)
        return HttpResponse(json_message, status=400)

def api_data(request):
    if request.method == "GET":
        queryset = models.Iris.objects.all()
        data = serialize('json', queryset)
        data_deserialized = json.loads(data)
        for element in data_deserialized:
            element['fields']['iris_class'] = IRIS_CLASSES[str(element['fields']['iris_class'])]
        data = json.dumps(data_deserialized)
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
