import requests, json

def addGame(gameid):
    cont = True
    
    with open("steam.json") as f:
        oldf = json.load(f)
        keylist = list(oldf.keys())
        for item in range(len(keylist)):
            if (keylist[item] == gameid):
                cont = False
    if cont:
        url = "https://store.steampowered.com/api/appdetails?appids=" + gameid + "&cc=br"
        response = requests.get(url)
        response = response.json()
        data = response[gameid]["data"]
        
        dic = {}
        with open("steam.json") as f:
            dic = json.load(f)
        
        dic[gameid] = {
                "id": str(data["steam_appid"]),
                "name": data["name"],
                "developers": data["developers"],
                "publishers": data["publishers"],
                "price": data["price_overview"]["final_formatted"],
                "release": data["release_date"]["date"]
            }
        

        object = json.dumps(dic, indent=4)

        with open("steam.json", "w") as f:
            f.write(object)
            
def deleteGame(gameid):
    dic = {}
    with open("steam.json", "r") as f:
            dic = json.load(f)
    del dic[gameid]
    object = json.dumps(dic, indent=4)
    with open("steam.json", "w") as f:
        f.write(object)
        
def updateGame(gameid):
    url = "https://store.steampowered.com/api/appdetails?appids=" + gameid + "&cc=br"
    response = requests.get(url)
    response = response.json()
    data = response[gameid]["data"]
    
    dic = {}
    with open("steam.json") as f:
        dic = json.load(f)
    
    dic[gameid] = {
            "id": str(data["steam_appid"]),
            "name": data["name"],
            "developers": data["developers"],
            "publishers": data["publishers"],
            "price": data["price_overview"]["final_formatted"],
            "release": data["release_date"]["date"]
        }
    

    object = json.dumps(dic, indent=4)

    with open("steam.json", "w") as f:
        f.write(object)
        