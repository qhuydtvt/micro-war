class ImageRenderer:
    def __init__(self, img):
        self.image = img
    
    def draw(self, screen, position):
        screen.blit(self.image, (position.x, position.y)) # () != []