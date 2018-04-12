from bases.vector2d import Vector2D

class GameObject:
  def __init__(self):
    self.renderer = None
    self.position = Vector2D(0, 0)
    self.active = True
    self.box_collider = None

  def draw(self, screen):
    if self.renderer:
        self.renderer.draw(screen, self.position)
    if self.box_collider:
      self.box_collider.draw(screen)
  
  def run(self):
      if self.box_collider:
        self.box_collider.position.copy2(self.position)

all_game_objects = []

def game_object_count():
  return len(all_game_objects)

def add_game_object(g_obj):
  all_game_objects.append(g_obj)

def clear_all():
  all_game_objects.clear()

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


def collide_with(box_collider, object_type):
  for game_object in all_game_objects:
    if game_object.active and \
      type(game_object) == object_type and \
      game_object.box_collider and \
      game_object.box_collider.collide_with(box_collider):
      return game_object
  return None


