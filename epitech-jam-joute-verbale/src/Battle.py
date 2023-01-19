from distutils.log import info
import pygame
import random
from src.Button import *
from src.InfosBattle import *
from src.character import Character
from src.Story import storyPannel

def getEnemyResponse(value, infosBt):
    if value < 0:
        return infosBt.enemy.winShout
    elif value > 0:
        return infosBt.enemy.looseShout
    else:
        return infosBt.enemy.middleShout

PATH_BACKGROUND = [
    "assets/background/rue.png",
    "assets/background/night_rue.png",
    "assets/background/paris.png",
]

def randomBackgroundSprite():
    nb = random.randint(0, len(PATH_BACKGROUND) - 1)
    return PATH_BACKGROUND[nb]

def battle(surface, level, player, enemy):
    infosBt = InfosBattle()
    infosBt.loadJson(level)

    path = randomBackgroundSprite()
    rue = Character(path, path, [0, 0])
    
    rue.setScale(1280, 720)
    
    shout = infosBt.enemy.middleShout
    confidence = 0
    storyPannel(surface, player, enemy, infosBt.enemy.description)
    player.setScale()
    enemy.setScale()
    for turn in infosBt.turns:
        surface.fill((255, 255, 255))
        surface.blit(rue.sprite, rue.logorect)
        running = True
        enemyText = EnemyTextBox(surface, 1280, 0, infosBt.enemy.name + ": " + shout)
        enemyPunch = EnemyTextBox(surface, 1280, 100, turn.punch)
        b1 = Button(surface, 80, 630, turn.responses[0].sentence)
        b2 = Button(surface, 700, 630, turn.responses[1].sentence)
        b3 = Button(surface, 80, 680, turn.responses[2].sentence)
        b4 = Button(surface, 700, 680, turn.responses[3].sentence)
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[0].value
                        shout = getEnemyResponse(turn.responses[0].value, infosBt)
                        running = False
                    if b2.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[1].value
                        shout = getEnemyResponse(turn.responses[1].value, infosBt)
                        running = False
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[2].value
                        shout = getEnemyResponse(turn.responses[2].value, infosBt)
                        running = False
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[3].value
                        shout = getEnemyResponse(turn.responses[3].value, infosBt)
                        running = False
            surface.blit(player.sprite, player.rect)
            surface.blit(enemy.sprite, enemy.rect)
            pygame.display.update()
    if confidence < 0:
        resultBattle = "Tu as perdu contre " + infosBt.enemy.name
        storyPannel(surface, player, enemy, resultBattle)
        return False
    elif confidence > 0:
        resultBattle = "Tu as gagné contre " + infosBt.enemy.name + ",\nun nouvel objet est diponible!"
    else:
        resultBattle = "Tu es passé tout juste contre " + infosBt.enemy.name + ",\ntu n'as pas réussi à dégoter un objet.."
        storyPannel(surface, player, enemy, resultBattle)
        return False
    storyPannel(surface, player, enemy, resultBattle)
    return True