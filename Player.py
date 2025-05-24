from pygame import transform, image
from os.path import join
class player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.img = image.load(join('Images', 'player', 'player.png')).convert_alpha()
        self.img = transform.flip(self.img, 90, 0)
        self.img = transform.scale(self.img, (self.width, self.height))