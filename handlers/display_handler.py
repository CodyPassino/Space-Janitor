import frame
import constants
import sprite_constants
import pygame
from small_meteor import Small_Meteor

from ship import Ship
from space_station import Space_Station

class Display_Handler():

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(constants.RESOLUTION)
        self.clock = pygame.Clock()
        self.ship = Ship()
        self.meteor = Small_Meteor([850,0])
        self.station = Space_Station([0,0,0])
        self.view = [] # Holds obj in player view

        self.scroll_x = 0
        self.scroll_y = 0

        # Init setup of player view
        frame.bg_loop(self) 
        self.display_hud()
        frame.render(self.clock)

    def keypressed(self):
        self.ship.dy = constants.STILL
        self.ship.dx = constants.STILL

        keys = pygame.key.get_pressed()
        is_turning = keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]
        is_moving = keys[pygame.K_SPACE]
        
        if is_turning:

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

            frame.bg_loop(self)

        if is_moving:
            #zoom
            if keys[pygame.K_SPACE]:
                for obj in self.view:
                    frame.zoom(self, obj)


         
        self.display_hud() 
        frame.render(self.clock)
        frame.get_panel(self.meteor)        


    def display_hud(self):
        frame.combine(self.screen, sprite_constants.MYHUD)
               

        

                
        
            
        

    
