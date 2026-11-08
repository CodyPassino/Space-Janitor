import frame
import constants
import sprite_constants
import pygame
from ship import Ship

class Display_Handler():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(constants.RESOLUTION)
        self.clock = pygame.Clock()
        self.ship = Ship()

        self.scroll_x = 0
        self.scroll_y = 0

        # Init setup of player view
        frame.bg_loop(self, self.ship.dx, self.ship.dy) 
        self.display_hud()
        frame.render(self.clock)

    def keypressed(self):
        self.ship.dy = constants.STILL
        self.ship.dx = constants.STILL

        keys = pygame.key.get_pressed()
        is_moving = keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]

        if is_moving:

            if keys[pygame.K_w]:
                self.ship.dy = constants.UP
            else:
                self.ship.dy = constants.STILL

            if keys[pygame.K_s]:
                self.ship.dy = constants.DOWN
           
            if keys[pygame.K_a]:
                self.ship.dx = constants.LEFT
            
            if keys[pygame.K_d]:
                self.ship.dx = constants.RIGHT
            

            self.screen.fill((255,0,0))

            frame.bg_loop(self, self.ship.dx, self.ship.dy) 
            self.display_hud() 
            frame.render(self.clock)        

    def display_hud(self):

        frame.combine(self.screen, sprite_constants.MYHUD)
               

        

                
        
            
        

    
