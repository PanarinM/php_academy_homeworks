from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from games.models import Game


def single_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.user.is_authenticated():
        game.views += 1
        game.save()
    return render(request, "single_game.html", {"game": game})


@login_required(login_url="/login")
def enter_game(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.user not in game.members.all():
        game.members.add(request.user)
        game.save()
    else:
        game.members.remove(request.user)
        game.save()
    #     games = Game.objects.filter(Q(creator_id=request.user.id)|Q(members__contains=request.user))
    #     games = Games.objects.filter(creator=request.user)
    #     games = Games.objects.filter(members__contains=request.user)
    return HttpResponseRedirect(reverse("single_game", kwargs={"game_id": game_id}))
