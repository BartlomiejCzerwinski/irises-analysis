from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("predict", views.predict, name="predict"),
    path("delete/<str:record_id>", views.delete, name="delete"),
    path("api/data", views.api_data, name="data"),
    path("api/data/<str:record_id>", views.api_delete, name="delete api")
    #path("api/predictions") TODO
]
