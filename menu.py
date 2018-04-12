from bases.game_objects import GameObject, clear_all
from bases.renderers.image_renderer import ImageRenderer

from scenes.gameplay_scene import init as gameplay_init
from input_manager import get_input_status
from utils import load_image

from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.renderer = ImageRenderer(load_image("menu.png"))
        self.position.copy(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    def run(self):
        GameObject.run(self)
        input_status = get_input_status()
        if input_status.x_pressed:
            clear_all()
            gameplay_init()
