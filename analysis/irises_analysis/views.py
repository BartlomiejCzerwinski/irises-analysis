from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods
import requests
import json
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import itertools
import os
import matplotlib
from analysis.settings import BASE_DIR

from . import forms
from . import models

IRIS_CLASSES = {'1': 'Setosa',
                '2': 'Versicolour',
                '3': 'Virginica'}

KNN_N_PARAMETER = 3

def index(request):
    api_get_data_url = 'http://127.0.0.1:8000/api/data'
    response = requests.get(api_get_data_url)
    #init_dataset("iris.csv")
    if response.status_code == 200:
        data = response.json()
        return render(request, "irises_analysis/index.html", {'data': data})
    return render(request, "irises_analysis/index.html")

def add(request):
    api_add_data_url = 'http://127.0.0.1:8000/api/data'
    form = forms.Form_add()
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
    form = forms.Form_predict()
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
            predicted_iris = {'sepal_length': sepal_length,
                                'sepal_width': sepal_width,
                                'petal_length': petal_length,
                                'petal_width': petal_width}
            plots = generate_pair_plots(predicted_iris)
            return render(request, "irises_analysis/predicted.html",
                            {'class': IRIS_CLASSES[predicted_class],
                             'plots': plots,
                             'knn_number': KNN_N_PARAMETER})
        else:
            return HttpResponse("400 error")
    return render(request, "irises_analysis/predict.html", {'form': form})

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

def api_predictions(request):
    sepal_length = float(request.GET.get('sepal_length'))
    sepal_width = float(request.GET.get('sepal_width'))
    petal_length = float(request.GET.get('petal_length'))
    petal_width = float(request.GET.get('petal_width'))
    form = forms.Form_predict({
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        })
    if form.is_valid():
        all_instances = models.Iris.objects.values_list('sepal_length', 'sepal_width', 'petal_length', 'petal_width')
        if len(all_instances) < KNN_N_PARAMETER:
            message = {"message": "Too small database for predictions"}
            json_message = json.dumps(message)
            return HttpResponse(json_message, status=400)
        labels = models.Iris.objects.values_list('iris_class', flat=True)
        knn_model = KNeighborsClassifier(n_neighbors=KNN_N_PARAMETER)
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
        new_iris_form = forms.Form_add(request.POST)
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

def api_delete(request, record_id):
    if request.method == "DELETE":
        try:
            iris = models.Iris.objects.get(id=record_id)
            iris.delete()
            return HttpResponse({"deleted_id": record_id}, status=200)
        except:
            return HttpResponse({"error": "Record not found"}, status=404)

def generate_pair_plots(predicted_iris):
    matplotlib.use('Agg')
    feature_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
    combinations = list(itertools.combinations(feature_names, 2))
    plots = []
    for combination in combinations:
        plots.append(generate_pair_plot(combination[0], combination[1], predicted_iris))
    return plots

def generate_pair_plot(x, y, predicted_iris):
    class_colors = {'Setosa': 'red', 'Versicolour': 'blue', 'Virginica': 'green', 'Predicted': 'purple'}
    iris_data = models.Iris.objects.all().values()
    iris_df = pd.DataFrame.from_records(iris_data)
    iris_df = iris_df.replace({"iris_class": {1: 'Setosa', 2: 'Versicolour', 3: 'Virginica'}})
    plt.plot(float(predicted_iris[x]), float(predicted_iris[y]), c='purple', marker="D", markersize=15)
    plt.axis('equal')
    plt.scatter(iris_df[x], iris_df[y], c=iris_df["iris_class"].map(class_colors))
    plt.xlabel(x)
    plt.ylabel(y)
    handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=label) for label, color in class_colors.items()]
    plt.legend(handles=handles)

    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    image_stream.seek(0)

    image_base64 = base64.b64encode(image_stream.read()).decode('utf-8')
    plt.clf()
    return image_base64

def init_dataset(dataset_name):
    file_path = os.path.join(BASE_DIR, dataset_name)
    df = pd.read_csv(file_path, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class'])
    for index, row in df.iterrows():
        iris = models.Iris(sepal_length=row['sepal_length'],
                                        sepal_width=row['sepal_width'],
                                        petal_length=row['petal_length'],
                                        petal_width=row['petal_width'],
                                        iris_class=row['iris_class'])
        iris.save()
