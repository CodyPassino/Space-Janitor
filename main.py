from handlers.display_handler import Display_Handler
import pygame
import sprite_constants

def main():
    display = Display_Handler()
    running = True
    
    display.display(sprite_constants.BG_1, 0, 0)
    while running:
        # checks for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        display.keypressed()

            

    pygame.quit()

if __name__ == '__main__':
    main()