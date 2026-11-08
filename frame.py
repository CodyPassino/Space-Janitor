import pygame


def move(screen, sprite,x, y):
        sprite_img = pygame.image.load(sprite).convert()
        screen.blit(sprite_img, (x, y))


    
    

