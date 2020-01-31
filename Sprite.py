import appgamekit as agk
from Color import Color

class Sprite:
    def __init__(self, image, x, y, width, height, angle, depth, centered, visible):
        if isinstance(image, str):
            if image != "NULL":
                self.image = agk.load_image(image)
        else:
            self.image = image

        if image != "NULL":
            self.id = agk.create_sprite(self.image)

        self.x = x
        self.y = y

        self.old_x = x
        self.old_y = y

        self.width = width
        self.height = height
        self.depth = depth
        self.angle = angle
        self.centered = centered
        self.visible = visible
        self.scale = 1.0
        self.color = Color(255, 255, 255, 255)

        if image != "NULL":
            self.update()

    def update(self):

        self.old_x = self.x
        self.old_y = self.y

        self.set_centered(self.centered)
        self.resize(self.width, self.height)
        self.set_position(self.x, self.y)
        self.set_depth(self.depth)
        self.set_visible(self.visible)

    def resize(self, width, height):
        self.width = width
        self.height = height
        agk.set_sprite_size(self.id, self.width, self.height)
        self.set_position(self.x, self.y)

    def set_position(self, x, y):
        self.old_x = self.x
        self.old_y = self.y
        self.x = x
        self.y = y

        if self.centered:
            centered_x = self.x - ((self.width  * self.scale) / 2)
            centered_y = self.y - ((self.height * self.scale) / 2)
            agk.set_sprite_position(self.id, centered_x, centered_y)
        else:
            agk.set_sprite_position(self.id, self.x, self.y)

    def set_angle(self, angle):
        self.angle = angle
        agk.set_sprite_angle(self.id, self.angle)

    def set_depth(self, depth):
        self.depth = depth
        agk.set_sprite_depth(self.id, self.depth)

    def set_scale(self, scale):
        self.scale = scale
        agk.set_sprite_size(self.id, self.width * self.scale, self.height * self.scale)
        self.position(self.x, self.y)

    def set_centered(self, centered):
        self.centered = centered
        agk.set_sprite_position(self.id, self.x, self.y)

    def set_visible(self, visible):
        self.visible = visible
        if self.visible:
            agk.set_sprite_visible(self.id, 1)
        else:
            agk.set_sprite_visible(self.id, 0)

    def get_width(self):
        return self.width * self.scale

    def get_height(self):
        return self.height * self.scale

    def set_proportional_size_by_width(self, width):
        self.scale = 1.0
        self.width = width
        image_ratio = agk.get_image_width(self.image) / agk.get_image_height(self.image)
        self.height = self.width * image_ratio
        self.resize(self.width, self.height)

    def set_proportional_size_by_height(self, height):
        self.scale = 1.0
        self.height = height
        image_ratio = agk.get_image_height(self.image) / agk.get_image_width(self.image)
        self.width = self.height * image_ratio
        self.resize(self.width, self.height)

    def get_centre_x(self):
        x = agk.get_sprite_x(self.id)
        half_width = agk.get_sprite_width(self.id) / 2
        centre_x = x + half_width
        return centre_x

    def get_centre_y(self):
        y = agk.get_sprite_y(self.id)
        half_height = agk.get_sprite_height(self.id) / 2
        centre_y = y + half_height
        return centre_y

    def get_centre_position(self):
        centre_x = self.get_centre_x()
        centre_y = self.get_centre_y()
        return centre_x, centre_y

    def set_color(self, color):
        self.color = color
        agk.set_sprite_color(self.id, self.color.red, self.color.green, self.color.blue, self.color.alpha)
