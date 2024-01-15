from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("predict", views.predict, name="predict"),
    path("api/data", views.data, name="data"),
    path("api/data/<str:record_id>", views.delete, name="delete")
    #path("api/predictions") TODO
]
