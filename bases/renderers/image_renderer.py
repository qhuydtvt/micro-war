from bases.vector2d import Vector2D

class ImageRenderer:
  def __init__(self, img):
    self.image = img
    self.anchor = Vector2D(0.5, 0.5)
    
  def draw(self, screen, position):
    x = position.x - (self.anchor.x * self.image.get_width())
    y = position.y - (self.anchor.y * self.image.get_height())
    screen.blit(self.image, (x, y))