from django.shortcuts import render, redirect
from .models import Game
from django.contrib import messages


def game_list(request):
    games = Game.objects.all()
    return render(request, 'joy/game_list.html', {'games': games})

def add_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        publisher = request.POST.get('publisher')
        release_date = request.POST.get('release_date')
        Game.objects.create(title=title, publisher=publisher, release_date=release_date)
        return redirect('game_list')
    return render(request,'joy/add_game.html')

def remove_game(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # Find the game by title
        try:
            game = Game.objects.get(title=title)
            game.delete()
            return redirect('game_list')
        except Game.DoesNotExist:
            error_message = f"No game found with title '{title}'."
            return render(request, 'joy/remove_game.html', {'error_message': error_message})
    return render(request, 'joy/remove_game.html')
