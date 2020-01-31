import appgamekit as agk
from Sprite import Sprite
from Text import Text

from Color import Color

class ImageButton:
    def __init__(self, image_name, text):
        self.name = ""
        self.id = ""
        self.sprite = -1
        self.images = []
        self.depth = 0
        self.active = True
        self.angle = 0.0
        self.is_switch = False
        self.is_visible = True
        self.is_centered = False
        self.fixed_to_screen = False
        self.update_with_orientation = True
        self.mode = 0

        self.image_frame = 0
        self.pressed_frame = 0
        self.update_if_pressed = True

        self.x = 0
        self.y = 0

        self.width = 200
        self.height = 50
        self.pressed_alpha = 0

        self.state = False
        self.pressed = False
        self.released = False

        self.border_visible = False

        self.border_color = Color(0, 0, 0, 0)
        self.border_size = 0
        self.border_image = 0
        self.border_sprites = []

        self.image_color = Color(255, 255, 0, 255)
        self.previous_state = False
        self.mode = 0

        if image_name == "":
            image_no = agk.create_image_color(255, 255, 255, 255)
            self.width = 200
            self.height = 50
        else:
            image_no = agk.load_image(image_name)
            self.width = agk.get_image_width(image_no)
            self.height = agk.get_image_weight(image_no)

        self.images.append(image_no)
        self.sprite = agk.create_sprite(image_no)

        self.sprite = Sprite(image_no, 0, 0, self.width, self.height, self.angle, self.depth, False, True)
        self.sprite.set_color(self.image_color)
        self.pressed_frame = 0
        self.pressed_alpha = 100
        self.alpha = 255

        self.text_size = 48
        self.text_color = Color(255, 255, 0, 255)
        self.text_offset_x = 0
        self.text_offset_y = 0
        self.text = Text(text, self.text_color, self.text_size, 0, 0, self.depth, True, True)

        self.border_visible = 0
        self.border_size = 5

        self.border_image = agk.create_image_color(255, 255, 255, 255)

        for i in range(0, 3):
            border_sprite = agk.create_sprite(self.border_image)
            agk.set_sprite_color(border_sprite, 0, 0, 0, 255)
            agk.set_sprite_visible(border_sprite, 0)
            self.border_sprites.append(border_sprite)

        self.update_if_pressed = True
        self.set_depth(0)

    def make_switch(self, x, y, width, height, alignment, depth ):
        self.is_switch = True
        self.is_centered = alignment
        self.set_size(width, height)
        self.set_depth(depth)
        self.set_position(x, y)

    def set_size(self, width, height):
        self.width = width
        self.height = height
        self.sprite.resize(self.width, self.height)
        self.update_position()

    def set_depth(self, depth):
        self.depth = depth
        self.sprite.set_depth(depth)
        self.text.set_depth(self.depth)

        for border_sprite in self.border_sprites:
            agk.set_sprite_depth(border_sprite, self.depth)

    def set_position(self, x, y):
        self.x = x
        self.y = y

        if self.is_centered:
            self.sprite.centered = 1
        else:
            self.sprite.centered = 0

        self.sprite.set_position(x, y)

        x = self.sprite.get_centre_x() + self.text_offset_x
        y = self.sprite.get_centre_y() + self.text_offset_y
        self.text.set_position(x, y)


    def update_position(self):
        self.set_image_button_position(self.x, self.y)

    def set_button_color(self, color):
        self.image_color = color
        self.sprite.set_color(self.image_color)

    def set_text_color(self, color):
        self.text_color = color
        self.text.set_color(color)
