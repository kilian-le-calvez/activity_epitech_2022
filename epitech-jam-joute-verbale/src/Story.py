import pygame
from src.Button import *
from src.character import Character

def textBox(screen, positionX, positionY, text):
        screen = screen
        font = pygame.font.SysFont("Arial", 40)
        text_render = font.render(text, 1, (0, 0, 0))
        x, y, w , h = text_render.get_rect()
        x = positionX
        y = positionY
        return screen.blit(text_render, (x, y))

def storyPannel(surface, monkey, enemy, text):
    rue = Character("assets/background/rue_sale.jpg", "assets/background/rue_sale.jpg", [0, 0])
    rue.setScale(1280, 720)
    surface.blit(rue.sprite, rue.rect)
    enemyText = applyBackLine(surface, 200, 500, text, 27)
    surface.blit(monkey.sprite, monkey.rect)
    surface.blit(enemy.sprite, enemy.rect)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.update()

def applyBackLine(screen, positionX, positionY, text, size):
    phrase = text
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, (200, 200, 200))
    x, y, w , h = text_render.get_rect()
    x = positionX
    y = positionY
    bulle = text_render.get_rect()
    x,y = bulle.topleft
    pygame.draw.rect(screen, (210, 225, 254), (x, y, w , h))
    for ligne in phrase.splitlines():
        x,y = screen.blit(font.render(ligne,1,(97,97,144)),(x,y)).bottomleft
        pygame.draw.rect(screen, (210, 225, 254), (x, y, w , h))
    return screen

