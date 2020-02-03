from django.db import models
from datetime import datetime


class News(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=256)
    # amount = models.FloatField(null=False, blank=False, default=None)
    # period = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
