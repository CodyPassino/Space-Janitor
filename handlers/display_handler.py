import sprite_constants
import pygame
class Display_Handler():

    def __init__(self):
        self.screen = pygame.display.set_mode((640,640))
        self.clock = pygame.Clock()
        self.delta_time = 0.1
    

    def display(self, sprite):
        running = True
        y = 0
        while running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((0,0,0))
            self.move(sprite, y*self.delta_time)

            self.clock.tick(60)
            pygame.display.flip()
            y += 1
            
        pygame.quit()

    def move(self, sprite, y):
        sprite_img = pygame.image.load(sprite).convert()
        self.screen.blit(sprite_img, (0, y))
