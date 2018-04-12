from bases.vector2d import Vector2D
from bases.game_objects import GameObject

from bases.renderers.rect_renderer import RectRenderer

class BoxCollider(GameObject):
    def __init__(self, width, height):
        GameObject.__init__(self)
        self.renderer = RectRenderer(width, height)
        self.width = width
        self.height = height
    
    def left(self):
        return self.position.x - self.width * 0.5
    
    def right(self):
        return self.position.x + self.width * 0.5
    
    def top(self):
        return self.position.y - self.height * 0.5
    
    def bot(self):
        return self.position.y + self.height * 0.5

    def collide_with(self, other):
        x_overlap = other.right() >= self.left() and other.left() <= self.right()
        y_overlap = other.bot() >= self.top() and other.top() <= self.bot()
        return x_overlap and y_overlap

