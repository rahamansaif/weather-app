from django.db import models


class Weather(models.Model):
    date = models.DateField()
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    temperatures = models.JSONField()
