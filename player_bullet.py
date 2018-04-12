from bases.game_objects import GameObject, collide_with
from bases.vector2d import Vector2D
from bases.renderers.image_renderer import ImageRenderer

from bases.physics.box_collider import BoxCollider

from utils import load_image
from enemy import Enemy

class PlayerBullet(GameObject):
    def __init__(self):
        GameObject.__init__(self)
        self.velocity = Vector2D(0, -10)
        self.renderer = ImageRenderer(load_image("player-bullet.png"))
        self.box_collider = BoxCollider(16, 16)
    
    def run(self):
        GameObject.run(self)
        self.position.add_up2(self.velocity)
        self.hitEnemy()
        self.deactive()
    
    def deactive(self):
        if self.position.y < 0:
            self.active = False

    def hitEnemy(self):
        enemy_to_hit = collide_with(self.box_collider, Enemy)
        if enemy_to_hit:
            enemy_to_hit.active = False
            self.active = False