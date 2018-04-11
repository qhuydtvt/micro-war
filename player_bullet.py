from bases.game_objects import GameObject
from bases.vector2d import Vector2D
from bases.renderers.image_renderer import ImageRenderer
from utils import load_image

class PlayerBullet(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.velocity = Vector2D(0, -10)
        self.renderer = ImageRenderer(load_image("player-bullet.png"))
    
    def run(self):
        GameObject.run(self)
        self.position.add_up2(self.velocity)
        self.deactive()
    
    def deactive(self):
        if self.position.y < 0:
            self.active = False
