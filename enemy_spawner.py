from bases.game_objects import GameObject, recycle
from bases.counter import Counter
from enemy import Enemy

from random import randint
from settings import SCREEN_WIDTH

class EnemySpawner(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.counter = Counter(100)
    
    def run(self):
        GameObject.run(self)

        if self.counter.run():
            self.counter.reset()
            enemy = recycle(Enemy)
            enemy.position.y = 0
            enemy.position.x = randint(0, SCREEN_WIDTH)