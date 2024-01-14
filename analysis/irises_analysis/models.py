from django.db import models

# Create your models here.

class Iris(models.Model):
    id = models.AutoField(primary_key=True)
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    sepal_width = models.FloatField()
    iris_class = models.IntegerField()
