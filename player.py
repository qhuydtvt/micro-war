from bases.game_objects import GameObject
from bases.renderers.image_renderer import ImageRenderer
from utils import load_image
from input_manager import get_input_status
from bases.vector2d import Vector2D

class Player(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.renderer = ImageRenderer(load_image("player.png"))
        self.velocity = Vector2D(0, 0)
    
    def run(self):
        GameObject.run(self)
        self.move()

    def move(self):
        self.velocity.x = 0
        self.velocity.y = 0

        input_status = get_input_status()
        
        if input_status.right_pressed:
            self.velocity.x += 5

        if input_status.left_pressed:
            self.velocity.x -= 5
        
        if input_status.down_pressed:
            self.velocity.y += 5
        
        if input_status.up_pressed:
            self.velocity.y -= 5
        
        self.position.x += self.velocity.x
        self.position.y += self.velocity.y
        
