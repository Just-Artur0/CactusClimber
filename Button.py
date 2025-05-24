from pygame import transform
class ui_button:
    def __init__(self, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.image = transform.scale(self.image, (self.width, self.height))