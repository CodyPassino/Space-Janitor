from handlers.display_handler import Display_Handler
import pygame
import sprite_constants
import frame

def main():
    display = Display_Handler()
    running = True
    
    
    while running:

        # checks for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        display.keypressed()

    pygame.quit()

if __name__ == '__main__':
    main()