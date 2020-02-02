import appgamekit as agk
from Player import Player
from SearchTree import SearchTree
from VisualEditor_ImageButton import *
from VisualEditor import VisualEditor
from Sprite import Sprite
from networking import Network
from Text import Text
from Controls import Controls
from Walls import Walls

class Game:
    def __init__(self, vis_editor):
        self.controls = Controls()
        self.type = ""
        self.vis_editor = vis_editor
        self.walls = Walls(self.vis_editor)

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
        self.vis_editor.open_scene(1)
        self.walls.load()

        if type == "boy" or type == "girl":
            self.spawn_player(type)

        self.update()

    def update(self):
        while True:
            self.controls.update()
            self.player.update(self.controls, self.walls.walls)


            agk.sync()



