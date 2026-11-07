import pygame
import constants

pygame.init()
screen = pygame.display.set_mode((650,650))
img = pygame.image.load(constants.file_metor).convert()

running = True
x = 0

clock = pygame.Clock()
delta_time = 0.1

while running:
    screen.blit(img, (x,90))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
