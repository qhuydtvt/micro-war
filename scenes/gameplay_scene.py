from enemy_spawner import EnemySpawner
from player import Player
from score import Score
from bases.game_objects import add_game_object

def init():
    add_game_object(Player())
    add_game_object(EnemySpawner())
    add_game_object(Score())