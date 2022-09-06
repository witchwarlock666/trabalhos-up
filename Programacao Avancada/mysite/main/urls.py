from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.listGames, name="index"),
    path("index/", views.listGames, name="index"),
    # path("b/", views.b, name="b"),
    path("newGame/", views.newGame, name="newGame"),
    path("listGames/", views.listGames, name="listGames"),
    path("game/<int:gameid>/", views.game, name="game"),
    path("updateGames/<int:gameid>/", views.updateGames, name="updateGames"),
    path("deleteGame/<int:gameid>/", views.deleteGame, name="deleteGame"),
    path("search/", views.search, name="search")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

