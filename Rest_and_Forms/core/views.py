from django.shortcuts import render
from django.db import models

from core.models import Configuration
from games.models import Game

from datetime import datetime


def get_config():
    return Configuration.objects.get()


def home(request):
    games = Game.objects.filter(date_end__gte=datetime.today().date()).annotate(members_number=models.Sum("members")).order_by("-views")[:10]
    return render(request, "home.html", {"configuration": get_config(),
                                         "games": games})
