import requests, json
from .models import Game

def createGame(id):
    idteste = "489830"
    cont = True

    # with open("games.json") as f:
    #     oldf = json.load(f)
    #     keylist = list(oldf.keys())
    #     for item in range(len(keylist)):
    #         if (keylist[item] == id):
    #             cont = False

    if cont:
        try:
            url = "https://store.steampowered.com/api/appdetails?appids=" + id + "&cc=br"
            print("1")
            response = requests.get(url)
            response = response.json()
            data = response[id]["data"]
            print("2")

            newdict = {
                id: {
                    "id": str(data["steam_appid"]),
                    "name": data["name"],
                    "developers": data["developers"],
                    "publishers": data["publishers"],
                    "price": data["price_overview"]["final_formatted"],
                    "release": data["release_date"]["date"],
                    # "background": data["background_raw"]
                }
            }
            print("3")
            
            gm = newdict[id]
            
            dev = ";".join(gm["developers"])
            pub = ";".join(gm["publishers"])
            
            game = Game(gameid=id, name=gm["name"], developers=dev, publishers=pub, price=gm["price"], release=gm["release"])
            print("4")
            game.save()
            print("5")
            
            print(Game.objects.all())

            # object = json.dumps(newdict, indent=4)

            # with open("games.json", "a") as f:
            #     f.write(object)
        except Exception as e:
            print(e)
            
def updateGame(id):
    oldGame = Game.objects.get(gameid=id)
    url = "https://store.steampowered.com/api/appdetails?appids=" + id + "&cc=br"
    response = requests.get(url)
    response = response.json()
    data = response[id]["data"]
    newdict = {
        id: {
            "id": str(data["steam_appid"]),
            "name": data["name"],
            "developers": data["developers"],
            "publishers": data["publishers"],
            "price": data["price_overview"]["final_formatted"],
            "release": data["release_date"]["date"],
            "background": data["background_raw"]
        }
    }
    
    gm = newdict[id]
            
    dev = ";".join(gm["developers"])
    pub = ";".join(gm["publishers"])
    
    newGame = Game(gameid=id, name=gm["name"], developers=dev, publishers=pub, price=gm["price"], release=gm["release"], background=gm["background"])
    
    oldGame.name = newGame.name
    oldGame.developers = newGame.developers
    oldGame.publishers = newGame.publishers
    oldGame.price = newGame.price
    oldGame.release = newGame.release
    oldGame.background = newGame.background
    
    oldGame.save()
