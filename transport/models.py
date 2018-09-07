from django.db import models


class TruckModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    tonnage = models.IntegerField(default=0)


class Truck(models.Model):
    number = models.CharField(max_length=10, unique=True)
    model = models.ForeignKey(TruckModel, on_delete=models.CASCADE)
    loaded = models.IntegerField(default=0)
