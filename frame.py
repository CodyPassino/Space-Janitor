import pygame
import constants

pygame.init()
screen = pygame.display.set_mode((800,800))
img_bird = pygame.image.load(constants.file_bird).convert()

running = True
x = 0

clock = pygame.Clock()
delta_time = 0.1

while running:
    screen.blit(img_bird, (x,90))

    x += 50 * delta_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.flip()
pygame.quit()
