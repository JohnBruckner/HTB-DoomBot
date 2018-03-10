import interface


class Data(object):

    def __init__(self, rawData):
        self.rawData = rawData

    def filterHealth(self):
        d = []
        for i in self.rawData:
            if i['type'] == 'Health Potion +1% health' or i['type'] == 'Green armor 100%':
                d.append(i)
        print(d)
        return d

    def filterAmmo(self):
        d = []
        for i in self.rawData:
            if i['type'] == 'Shotgun shells' or i['type'] == 'Ammo clip' or i['type'] == 'Box of Rockets':
                d.append(i)
        print(d)
        return d

    def filterWeapons(self):
        d = []
        for i in self.rawData:
            if i['type'] == 'Shotgun' or i['type'] == 'Chainsaw' or i['type'] == 'Rocket launcher':
                d.append(i)
        print(d)
        return d

    def filterPlayers(self):
        d = []
        for i in self.rawData:
            if i['type'] == 'Player':
                d.append(i)
        print(d)
        return d

    def filterBy(self, fltr):
        if fltr.lower() == "weapons":
            return self.filterWeapons()
        elif fltr.lower() == "health":
            return self.filterHealth()
        elif fltr.lower() == "ammo":
            return self.filterAmmo()
        else:
            return self.filterPlayers()
