import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT

from utils import load_image
from bases.game_objects import run_all, draw_all, add_game_object, game_object_count
from input_manager import process_event, get_input_status
from player import Player


SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

clock = pygame.time.Clock()

pygame.init() # Graphics, Sound
pygame.display.set_caption("Micro-war")
screen = pygame.display.set_mode(SIZE)

loop = True

player = Player()
add_game_object(player)

# game loop
while loop:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            process_event(event)

    screen.fill((255, 255, 255))

    run_all()
    draw_all(screen)

    clock.tick(60)
    pygame.display.flip()
