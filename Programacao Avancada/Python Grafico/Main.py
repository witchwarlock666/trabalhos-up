import json
import PySimpleGUI as psg
import Data

psg.theme('Topanga')

globalGame = ""

def make_menu():
    layout = [[psg.Button('List', size=(10, 1))],
              [psg.Button('New Game', size=(10, 1))],
              [psg.Button('Close', size=(10, 1))]]

    return psg.Window("Steam Games Database", layout, finalize=True, size=(400,110))


def make_new():
    layout = [[psg.Text('New Game')],
              [psg.Text('Appid'), psg.InputText(key='ID')],
              [psg.Button('Submit'), psg.Button('Home')]]

    return psg.Window("New Game", layout, finalize=True)


def make_list():
    keylist = []
    with open("steam.json") as f:
        j = json.load(f)
        keylist = list(j.keys())
    layout = [[psg.Text('Game List')],
              [psg.Listbox(values=keylist, key='gID', select_mode='extended', size=(30, 6))],
              [psg.Button('Open'), psg.Button('Home')]]
    return psg.Window("Game List", layout, finalize=True)


def make_game(game):
    dic = {}
    with open("steam.json") as f:
        j = json.load(f)
        dic = j[game[0]]
    developers = ""
    publishers = ""
    
    for dev in dic["developers"]:
        developers += dev + ", "
    developers = developers[:-2]
    
    for pub in dic["publishers"]:
        publishers += pub + ", "
    publishers = publishers[:-2]
    
    layout = [[psg.Text(game)],
              [psg.Text("Appid:"), psg.Text(dic["id"])],
              [psg.Text("Name:"), psg.Text(dic["name"])],
              [psg.Text("Developers:"), psg.Text(developers)],
              [psg.Text("Publishers:"), psg.Text(publishers)],
              [psg.Text("Price:"), psg.Text(dic["price"])],
              [psg.Text("Release:"), psg.Text(dic["release"])],
              [psg.Button('Update'), psg.Button('Delete'), psg.Button('Home')]]
    return psg.Window("Game Info", layout, finalize=True, size=(400,300))


window1, window2, window3, window4 = make_menu(), None, None, None

while True:

    window, event, values = psg.read_all_windows()

    if window == window1 and event in (psg.WIN_CLOSED, 'Close'):
        break

    if window == window1:
        if event == 'List':
            window1.hide()
            window2 = make_list()
        if event == 'New Game':
            window1.hide()
            window3 = make_new()

    if window == window2:
        if event == 'Open':
            game = values['gID']
            globalGame = game[0]
            window2.close()
            window4 = make_game(game)
        if event in (psg.WIN_CLOSED, 'Home'):
            window2.close()
            window1.un_hide()

    if window == window3:
        if event == 'Submit':
            game = values["ID"]
            Data.addGame(game)
            psg.popup("Game Added!")
            window3.close()
            window1.un_hide()
        if event in (psg.WIN_CLOSED, 'Home'):
            window3.close()
            window1.un_hide()

    if window == window4:
        if event == 'Update':
            Data.updateGame(globalGame)
            window4.close()
            window4 = make_game(game)
            psg.popup("Game Updated!")
        if event == 'Delete':
            Data.deleteGame(globalGame)
            psg.popup("Game Deleted!")
            window4.close()
            window1.un_hide()
        if event in (psg.WIN_CLOSED, 'Home'):
            window4.close()
            window1.un_hide()

window.close()
