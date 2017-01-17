from django.conf.urls import url

from games.views import single_game, enter_game

urlpatterns = [
    url(r'^(?P<game_id>[\d]+)/$', single_game, name="single_game"),
    url(r'^enter/(?P<game_id>[\d]+)/$', enter_game, name="enter_game"),
]
