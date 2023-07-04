from django.shortcuts import render

from .models import Gericht

def speisekarte(request):
    gerichte = Gericht.objects.all()
    context = {"gerichte":gerichte}
    return render(request, "Speisekarte/speisekarte.html", context)