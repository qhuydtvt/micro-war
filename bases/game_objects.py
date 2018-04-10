from bases.vector2d import Vector2D

class GameObject:
    def __init__(self):
        self.renderer = None
        self.position = Vector2D(0, 0)

    def draw(self, screen):
        if self.renderer:
            self.renderer.draw(screen, self.position)
    
    def run(self):
        pass

all_game_objects = []

def add_game_object(g_obj):
    all_game_objects.append(g_obj)

def run_all():
    for game_object in all_game_objects:
        game_object.run()


def draw_all(screen):
    for game_object in all_game_objects:
        game_object.draw(screen)