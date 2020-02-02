import appgamekit as agk

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.sprite = 0
        self.speed = 3.0