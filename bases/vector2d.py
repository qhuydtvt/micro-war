class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add_up(self, x, y):
        self.x += x
        self.y += y
    
    def add_up2(self, other):
        self.x += other.x
        self.y += other.y
    
    def copy(self, x, y):
        self.x = x
        self.y = y
    
    def copy2(self, other):
        self.x = other.x
        self.y = other.y