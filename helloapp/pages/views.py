import numpy as np

from django.shortcuts import render
# Create your views here.
from .game import Game
from django.http import JsonResponse


def homeRequest(request):
    if request.GET.get('Right'):
        print('Right clicked')
    if request.GET.get('Down'):
        print('Down clicked')
    return render(request, 'home.html')

def valueFuncRequest(request, dim, start, goal):
    game = Game(dim, start, goal, action_cost=-1)
    value_func = game.calculate_value_function()

    data = {
        "val_func": np.hstack(value_func).tolist(),
        "goal_reward": str(game.goal_reward),
    }
    return JsonResponse(data)
