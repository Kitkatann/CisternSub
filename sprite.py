from vector2D import Vector2D

class Sprite:
    def __init__(self, position, foreground):
        self.position = position.Clone()
        self.foreground = foreground