from django.db import models

# Create your models here.

class Temperature(models.Model):
    temperature = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.temperature} at {self.timestamp}"  
    