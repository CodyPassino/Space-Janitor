import pygame
import constants
import math
import sprite_constants

def setpos(screen, sprite,x, y):
        x = x * constants.DELTA_TIME
        y = y * constants.DELTA_TIME
        sprite_img = pygame.image.load(sprite).convert()

        screen.blit(sprite_img, (x, y))

def render(clock):
        clock.tick(constants.FPS)
        pygame.display.flip()

def combine(screen, sprite_location_d):
        for path in sprite_location_d:
                img = pygame.image.load(path).convert_alpha()
                screen.blit(img, sprite_location_d[path])

def bg_loop(display, d_x, d_y):

        bg = pygame.image.load(sprite_constants.BG_1).convert()
        bg_width = bg.get_width()
        bg_height = bg.get_height()

        panels_x = math.ceil(constants.RESOLUTION[0]/bg_width) + 2
        panels_y = math.ceil(constants.RESOLUTION[1]/bg_height) + 2

        display.scroll_x += constants.SHIP_TURN_SPEED * d_x
        display.scroll_y += constants.SHIP_TURN_SPEED * d_y

        if abs(display.scroll_x) > bg_width:
                display.scroll_x = 0

        if abs(display.scroll_y) > bg_height:
                display.scroll_y = 0

        for x_panel, y_panel in zip(range(panels_x), range(panels_y)):
                new_y = y_panel * bg_height + display.scroll_y - bg_height
                new_x = x_panel * bg_width + display.scroll_x - bg_width

                display.screen.blit(bg,(new_x, new_y))
        

        
    
    

