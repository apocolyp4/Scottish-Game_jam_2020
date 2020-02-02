import appgamekit as agk
from Player import Player
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Controls import Controls

class Game:
    def __init__(self, vis_editor):
        self.controls = Controls()
        self.type = ""
        self.vis_editor = vis_editor
        self.walls = []

    def spawn_player(self, type):

        boy_sprite = self.vis_editor.get_entity_id("Boy", 1)
        girl_sprite = self.vis_editor.get_entity_id("Girl", 1)
        self.boy_player = Player("boy", boy_sprite)
        self.girl_player = Player("girl", girl_sprite)

        self.type = type
        if self.type == "girl":
            self.player = self.girl_player
        else:
            self.player = self.boy_player

    def start(self, type):
        self.walls = []
        self.vis_editor.open_scene(1)

        if type == "boy" or type == "girl":
            self.spawn_player(type)

        self.update()

    def update(self):
        while True:
            self.controls.update()
            self.player.update(self.controls)


            agk.sync()



