from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .steam import createGame, updateGame
from .forms import addGame, searchGame
from .models import Game

# Create your views here.

# def index(res):
#     message = ""
#     if res.method == "POST":
#         form = searchGame(res.POST)
#         print(form)
#         cl = form.cleaned_data["appid"]
#         try:
#             game = Game.objects.get(gameid=cl)
#             return HttpResponseRedirect(f"/game/{cl}")
#         except:
#             message = "Game does not exist!"
#             return render(res, "main/index.html", {"form": form, "message": message})
#     else:
#         form = searchGame()
#     return render(res, "main/index.html", {"form": form, "message": message})

def b(res):
    return render(res, "main/_layout.html", {})

def newGame(res):
    if res.method == "POST":
        form = addGame(res.POST)
        
        if form.is_valid():
            cl = form.cleaned_data["appid"]
            createGame(cl)
        return HttpResponseRedirect(f"/game/{cl}")
    else:
        form = addGame()
    return render(res, "main/newGame.html", {"form": form})

def listGames(res):
    games = Game.objects.all()
    return render(res, "main/listGames.html", {"games": games})

def game(res, gameid):
    game = Game.objects.get(gameid=gameid)
    
    publishers = game.publishers.split(";")
    developers = game.developers.split(";")
    
    return render(res, "main/game.html", {"game": game, "publishers": publishers, "developers": developers})

def updateGames(res, gameid):
    gameid = str(gameid)
    updateGame(gameid)
    game = Game.objects.get(gameid=gameid)
    
    publishers = game.publishers.split(";")
    developers = game.developers.split(";")
    return HttpResponseRedirect(f"/game/{gameid}")

def deleteGame(res, gameid):
    gameid = str(gameid)
    game = Game.objects.get(gameid=gameid)
    game.delete()
    return HttpResponseRedirect("/")

def searchGames(query):
    gameList = []
    games = Game.objects.all()
    
    for game in games:
        developers = game.developers.split(";")
        publishers = game.publishers.split(";")
        year = game.release.split(" ")[-1]
        cont = True
        if cont:
            if query in game.gameid or query.upper() in game.name.upper() or query in game.price or query in game.release or query in year:
                gameList.append(game)
                cont = False
            
        if cont:
            for dev in developers:
                if query.upper() in dev.upper():
                    gameList.append(game)
                    cont = False
        if cont:
            for pub in publishers:
                if query.upper() in pub.upper():
                    gameList.append(game)
    
    return gameList
            
def search(res):
    if res.method == "POST":
        print(res.POST)
        form = searchGame(res.POST)
        print(form)
        query = form.cleaned_data["query"]
        gameList = searchGames(query)
    else:
        return HttpResponseRedirect("/")
    
    return render(res, "main/search.html", {"gameList": gameList})
