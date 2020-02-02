from Player import Player

class Game:
    def __init__(self):
        self.boy_player = Player()
        self.girl_player = Player()

    def spawn_player(self, type):
        self.player.type = type