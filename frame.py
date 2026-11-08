import pygame
import constants
def move(screen, sprite,x, y):
        x = x * constants.DELTA_TIME
        y = y * constants.DELTA_TIME
        sprite_img = pygame.image.load(sprite).convert()

        screen.blit(sprite_img, (x, y))

def render(clock):
        clock.tick(60)
        pygame.display.flip()

def combine(screen, sprite_location_d):
        for path in sprite_location_d:
                img = pygame.image.load(path).convert_alpha()
                screen.blit(img, sprite_location_d[path])



    
    

