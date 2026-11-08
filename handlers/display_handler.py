import frame
import constants
import sprite_constants
import pygame
class Display_Handler():

    def __init__(self):
        self.screen = pygame.display.set_mode(constants.RESOLUTION)
        self.clock = pygame.Clock()
        self.delta_time = 0.1
    

    def display(self, sprite):
        running = True
        x = 0
        y = 0
        while running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((255,0,0))
            frame.move(self.screen, sprite, x *self.delta_time, y*self.delta_time)

            self.clock.tick(60)
            pygame.display.flip()
            y += 5
            
        pygame.quit()

    
