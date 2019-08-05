import pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def draw():
    pass


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
