from django.shortcuts import render

def index(request):
    return render(request, '../templates/index.html')

def game(request):
    return render(request, 'game/game.html')