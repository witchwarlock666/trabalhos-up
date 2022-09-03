import requests, json

idteste = "489830"
cont = True

gameid = input("Game Id: ")

# with open("games.json") as f:
#     oldf = json.load(f)
#     keylist = list(oldf.keys())
#     for item in range(len(keylist)):
#         if (keylist[item] == gameid):
#             cont = False

if cont:
    try:
        url = "https://store.steampowered.com/api/appdetails?appids=" + gameid + "&cc=br"
        response = requests.get(url)
        response = response.json()
        # data = response[gameid]["data"]

        # newdict = {
        #     gameid: {
        #         "id": str(data["steam_appid"]),
        #         "name": data["name"],
        #         "developers": data["developers"],
        #         "publishers": data["publishers"],
        #         "price": data["price_overview"]["final_formatted"],
        #         "release": data["release_date"]["date"]
        #     }
        # }

        # object = json.dumps(newdict, indent=4)
        object = json.dumps(response, indent=4)

        with open("steam.json", "a") as f:
            f.write(object)
    except Exception as e:
        print(e)
