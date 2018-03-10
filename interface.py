import json
import requests
import time


class Interface(object):

    def __init__(self, port):
        self.port = port
        self.baseAddr = "http://localhost:" + str(port)

    # Gets the data form the game, returning it as a structure same as the json in REST description
    def getPlayers(self):
        r = requests.get(str(self.baseAddr) + "/api/players")
        data = r.json()
        return data
    # Gets the objects present in the game
    def getWorldObjects(self):
        r = requests.get(str(self.baseAddr) + "/api/world/objects")
        data = r.json()
        return data

    # Posts the action into the game
    # Post data needs to be sent as json
    def playerAction(self, action, amount):
        data = {'type': action,
                'amount': amount}
        jsonData = json.dumps(data)
        r = requests.post(self.baseAddr + "/api/player/actions", data=jsonData)
        # print(r)


if (__name__ == '__main__'):
    i = Interface(6001)
    players = i.getPlayers()
    # sTime = time.time()
    # print(len(players))
    for j in range(20):
        # startTime = time.time()
        i.playerAction("shoot", 1)
        i.playerAction("turn-right", 20)
        # elapsedTime = time.time() - startTime
        # print(elapsedTime)
    # print(time.time()-sTime)
    # print(i.getPlayers())
    print(i.getWorldObjects())
