import pygame


SIZE = (600, 800)

clock = pygame.time.Clock()

pygame.init() # Graphics, Sound
pygame.display.set_caption("Micro-war")
screen = pygame.display.set_mode(SIZE)

loop = True

# game loop
while loop:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
    
    clock.tick(60)
    pygame.display.flip()
