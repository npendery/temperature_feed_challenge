from django.db import models

# Create your models here.

class Temperature(models.Model):
    value = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.value} at {self.timestamp}"  
    