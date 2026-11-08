from handlers.display_handler import Display_Handler
import pygame

from sprite_constants import TITLECARD

def main():
    display = Display_Handler()
    running = True
    showing_titlecard = True

    titlecard_img = pygame.image.load(TITLECARD).convert()
    while running:
        
        # checks for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if showing_titlecard:
                    showing_titlecard = False
                # Shortcut to quit - "q"
                if event.key == pygame.K_q:
                    running = False

        # Checks if any keys pressed and edits visuals accordingly
        display.keypressed()

    pygame.quit()

if __name__ == '__main__':
    main()