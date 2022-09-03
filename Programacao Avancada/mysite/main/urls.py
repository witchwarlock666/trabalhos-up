from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path("b/", views.b, name="b"),
    path("newGame/", views.newGame, name="newGame"),
    path("listGames/", views.listGames, name="listGames"),
    path("game/<int:gameid>/", views.game, name="game")
]

