import frame
import constants
import sprite_constants
import pygame
from ship import Ship
class Display_Handler():

    def __init__(self):
        self.screen = pygame.display.set_mode(constants.RESOLUTION)
        self.clock = pygame.Clock()
        self.ship = Ship()

    def display(self, sprite, x, y):
        
        self.screen.fill((255,0,0))
        frame.move(self.screen, sprite, x, y)

        frame.render(self.clock)

    def keypressed(self):
        keys = pygame.key.get_pressed()
        is_moving = keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]

        if is_moving:

            if keys[pygame.K_w]:
                self.ship.y += constants.SHIP_TURN_SPEED
            if keys[pygame.K_s]:
                self.ship.y -= constants.SHIP_TURN_SPEED
            if keys[pygame.K_a]:
                self.ship.x += constants.SHIP_TURN_SPEED
            if keys[pygame.K_d]:
                self.ship.x -= constants.SHIP_TURN_SPEED
        
            self.display(sprite_constants.BG_1, self.ship.x, self.ship.y) 
    
                
        
            
        

    
