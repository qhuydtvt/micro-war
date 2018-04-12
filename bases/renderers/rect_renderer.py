from bases.renderers.colors import RED
import pygame

class RectRenderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = RED
        self.line_width = 1
    
    def draw(self, screen, position):
        rect = (position.x - self.width / 2, position.y - self.height / 2, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect, self.line_width)
