from bases.vector2d import Vector2D

class GameObject:
  def __init__(self):
    self.renderer = None
    self.position = Vector2D(0, 0)
    self.active = True

  def draw(self, screen):
    if self.renderer:
        self.renderer.draw(screen, self.position)
  
  def run(self):
      pass

all_game_objects = []

def game_object_count():
  return len(all_game_objects)

def add_game_object(g_obj):
  all_game_objects.append(g_obj)

def run_all():
  for game_object in all_game_objects:
    if game_object.active:
      game_object.run()


def recycle(request_type):
  for game_object in all_game_objects:
    if (not game_object.active) and type(game_object) == request_type:
      game_object.active = True
      return game_object

  new_object = request_type()
  add_game_object(new_object)
  return new_object

def draw_all(screen):
  for game_object in all_game_objects:
    if game_object.active:
      game_object.draw(screen)