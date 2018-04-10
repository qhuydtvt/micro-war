from bases.game_objects import GameObject
from bases.renderers.image_renderer import ImageRenderer
from utils import load_image

class Player(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.renderer = ImageRenderer(load_image("player.png"))
    
    def run(self):
        GameObject.run(self)
        self.position.x += 2
