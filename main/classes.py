## Classes #######################################################################

class Player(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.troops = 0

class Territory(object):
    def __init__(self, name, troops, player):
        self.name = name
        self.owner = player
        self.troops = int(troops)


class Map(object):
    def __init__(self):
        pass
