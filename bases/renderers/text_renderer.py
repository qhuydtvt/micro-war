import pygame

class TextRenderer:
    def __init__(self, text, color):
        self.text = text
        self.color = color
        self.font = pygame.font.SysFont("consolas", 16)
    
    def draw(self, screen, position):
        label = self.font.render(self.text, 0, self.color)
        screen.blit(label, (position.x, position.y))
