from bases.game_objects import GameObject
from bases.renderers.image_renderer import ImageRenderer
from bases.counter import Counter
from bases.vector2d import Vector2D

from settings import SCREEN_HEIGHT

from utils import load_image

class Enemy(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.velocity = Vector2D(0, 2)
        self.renderer = ImageRenderer(load_image("enemy.png"))
    
    def run(self):
        GameObject.run(self)
        self.position.add_up2(self.velocity)
        if self.position.y > SCREEN_HEIGHT:
            self.active = False