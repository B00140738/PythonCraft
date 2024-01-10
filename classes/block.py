from ursina import *

class Block(Button):

    type = ''

    def __init__(self, color, model, position, texture, type):
        super().__init__()
        self.color = color
        self.model = model
        self.position = position
        self.texture = texture
        self.type = type
    
    def get_type(self):
        return self.type

