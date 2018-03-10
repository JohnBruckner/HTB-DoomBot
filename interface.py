import json
import requests

class Interface:

    def __init__(self, port):
        self.port = port
        self.baseAddr = "http://localhost:" + str(port)

    # Gets the data form the game, returning it as a structure same as the json in REST description
    def getPlayers(self):
        r = requests.get(self.baseAddr + "/api/players")
        data = r.json()
        return data

    # Posts the action into the game
    # Note: so far it sometimes doesn't work, I will need to debug it later
    def playerAction(self, action, amount):
        r = requests.post(self.baseAddr + "/api/player/actions", data = {'action':action, 'amount':amount})

if (__name__ == '__main__'):
    i = Interface(6001)
    i.getPlayers()
    i.playerAction("turn-left", 10)
    i.playerAction("forward", 5)
