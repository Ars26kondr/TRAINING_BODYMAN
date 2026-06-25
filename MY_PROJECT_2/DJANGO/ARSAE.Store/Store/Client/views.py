from django.shortcuts import render
from .models import Game
def index(r):
    game=Game.objects.all()
    bannergame=Game.objects.get(id=2)
    return render(r, 'index.html', {'Game': game, 'banner': bannergame})
# Create your views here.
def RE2(r, id):
    game=Game.objects.get(id=id)
    return render(r, 'RE2og.html', {'game': game})
def acsories(r):
    game=Game.objects.all()
    return render(r, 'acsories.html', {'game': game})
def search_results(r):
    game_info=r.GET.get("A")
    results=[]
    if game_info:
        results=Game.objects.filter(Name__icontains=game_info)
    return render(r, 'results.html', {'games': results})