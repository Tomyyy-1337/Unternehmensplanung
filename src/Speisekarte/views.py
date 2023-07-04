from django.shortcuts import render

from .models import Gericht, Kategorie

def speisekarte(request):
    gerichte = Gericht.objects.all()
    context = {"gerichte":gerichte, "kategorien":Kategorie.objects.all()}
    return render(request, "Speisekarte/speisekarte.html", context)