import appgamekit as agk
from calculations import *
from CollisionDetection import *
from Sprite import Sprite
from copy import copy

class Player:
    def __init__(self, name, sprite):
        self.name = name
        self.health = 100
        self.sprite = sprite
        self.speed = 6.0
        self.x = agk.get_sprite_x(sprite)
        self.y = agk.get_sprite_y(sprite)

        self.old_x = 0
        self.old_y = 0
        self.old_vel_x = 0
        self.old_vel_y = 0

    def update(self, controls, walls):


        if controls.game_pad.left_force > 0.1:
            angle = controls.game_pad.left_angle
            distance = self.speed * controls.game_pad.left_force
            velocity = get_velocity(angle, distance)
            self.old_x = copy(self.x)
            self.old_y = copy(self.y)

            self.x += velocity[0]
            self.y += velocity[1]

            if check_wall_collision(self.sprite, walls):
                distance_x = self.x - self.old_x
                distance_y = self.y - self.old_y
                
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

