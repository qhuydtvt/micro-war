from bases.game_objects import GameObject
from bases.renderers.text_renderer import TextRenderer
from bases.renderers.colors import RED
from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Score(GameObject):
    value = 0
    def __init__(self):
        GameObject.__init__(self)
        self.position.copy(SCREEN_WIDTH - 100, 40)
        self.renderer = TextRenderer("", RED)
    
    def run(self):
        GameObject.run(self)
        self.renderer.text = "Score: {0}".format(Score.value)
