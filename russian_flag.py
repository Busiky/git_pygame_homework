import pygame

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)


def draw():
    pygame.draw.rect(screen, pygame.Color('#65350f'), (20, 20, 30, 460))
    pygame.draw.rect(screen, pygame.Color('red'), (50, 220, 430, 100))
    pygame.draw.rect(screen, pygame.Color('blue'), (50, 120, 430, 100))
    pygame.draw.rect(screen, pygame.Color('white'), (50, 20, 430, 100))

    pygame.draw.rect(screen, pygame.Color((0, 0, 0)), (440, 440, 30, 4), 2)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
