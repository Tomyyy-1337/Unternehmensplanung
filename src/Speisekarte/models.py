from django.db import models

class Kategorie(models.Model):
    name = models.CharField(max_length=200)
    priority = models.IntegerField();

    def __str__(self):
        return self.name

class Gericht(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True) 
    preis = models.FloatField()
    kategorie = models.ForeignKey(Kategorie, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name