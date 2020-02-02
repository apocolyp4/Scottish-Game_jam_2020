import appgamekit as agk
from calculations import *
from Sprite import Sprite

class Player:
    def __init__(self, name, sprite):
        self.name = name
        self.health = 100
        self.sprite = sprite
        self.speed = 6.0
        self.x = 0
        self.y = 0

    def update(self, controls):
        if controls.game_pad.left_force > 0.1:
            angle = controls.game_pad.left_angle
            distance = self.speed * controls.game_pad.left_force
            velocity = get_velocity(angle, distance)
            self.x += velocity[0]
            self.y += velocity[1]


        if controls.game_pad.right_force > 0.1:
            angle = controls.game_pad.right_angle
            agk.set_sprite_angle(self.sprite, angle)

        zoom = 0.5
        agk.set_view_zoom(0.5)
        cam_x = self.x + (agk.get_virtual_width() / (2 * zoom))
        cam_y = self.y + (agk.get_virtual_height() / (2 * zoom))
        agk.set_sprite_position(self.sprite, cam_x, cam_y)

        agk.set_view_offset(self.x, self.y)

        if controls.game_pad.right_trigger > 0.1:
            agk.print_value("fire")

