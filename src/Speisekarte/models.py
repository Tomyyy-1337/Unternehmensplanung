from django.db import models

class Gericht(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    preis = models.FloatField()

    def __str__(self):
        return self.name
    