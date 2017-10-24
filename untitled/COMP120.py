import pygame
import random

from random import randint


pygame.init()

def spritegenerator():
    intTop = randint(1,4)
    intMiddle = randint(1,4)
    intBottom = randint(1,4)

    if intTop == 1:
        imgTop = pygame.image.load (("T1.png"))
    elif intTop == 2:
        imgTop = pygame.image.load (("T2.png"))
    elif intTop == 3:
        imgTop = pygame.image.load (("T3.png"))
    elif intTop == 4:
        imgTop = pygame.image.load (("T4.png"))

    if intMiddle == 1:
        imgMiddle = pygame.image.load (("M1.png"))
    elif intMiddle == 2:
        imgMiddle = pygame.image.load (("M2.png"))
    elif intMiddle == 3:
        imgMiddle = pygame.image.load (("M3.png"))
    elif intMiddle == 4:
        imgMiddle = pygame.image.load (("M4.png"))

    if intBottom == 1:
        imgBottom = pygame.image.load (("B1.png"))
    elif intBottom == 2:
        imgBottom = pygame.image.load (("B2.png"))
    elif intBottom == 3:
        imgBottom = pygame.image.load (("B3.png"))
    elif intBottom == 4:
        imgBottom = pygame.image.load (("B4.png"))

    screen.blit(imgTop,(0, 0))
    screen.blit(imgMiddle,(0,100))
    screen.blit(imgBottom,(0,200))
    pygame.display.flip()
    pygame.image.save(screen,"Random.png")
    return







(width, height) = (100, 300)
screen = pygame.display.set_mode((width, height))
pygame.display.flip()

spritegenerator()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False