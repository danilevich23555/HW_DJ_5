from django.db import models



class Sensor(models.Model):
    name = models.TextField()
    description = models.TextField()

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()