import random
import pygame
import pygame_menu

from src.character import Character
from src.Battle import battle
from src.InfosBattle import LEVELS, InfosBattle
from src.Story import storyPannel
from src.Button import *

WIDTH = 1280
HEIGHT = 720
lvl = []

def choose_menu():
    w, h = pygame.display.get_surface().get_size()
    ##gorille
    gorille = Character("assets/gorilla/gorilla_base.png",
                        "assets/gorilla/gorilla_base.png", [200, 300])
    ##clodo
    clodo = Character("assets/enemies/full_clodo.png",
                      "assets/enemies/head_clodo.png", [800, 300])
    clodo_button = pygame.Rect(10, 10, 300, 300)
    clodo_surf = pygame.Surface(clodo_button.size)
    ##titi
    titi = Character("assets/enemies/full_titi.png",
                     "assets/enemies/head_titi.png", [800, 300])
    titi_button = pygame.Rect(((w - 300) / 2), 10, 300, 300)
    titi_surf = pygame.Surface(titi_button.size)
    ##ronald
    ronald = Character("assets/enemies/full_ronald.png",
                       "assets/enemies/head_ronald.png", [800, 300])
    ronald_button = pygame.Rect(10, (h - 300), 300, 300)
    ronald_surf = pygame.Surface(ronald_button.size)
    ##maman
    maman = Character("assets/enemies/full_maman_enfant.png",
                      "assets/enemies/head_maman_enfant.png", [800, 300])
    maman_button = pygame.Rect(((w - 300) / 2), (h - 300), 300, 300)
    maman_surf = pygame.Surface(maman_button.size)
    #gaston
    gaston = Character("assets/enemies/full_gaston.png",
                       "assets/enemies/head_gaston.png", [800, 300])
    gaston_button = pygame.Rect((w - 300), 10, 300, 300)
    gaston_surf = pygame.Surface(gaston_button.size)
    #noel
    noel = Character("assets/enemies/full_noel.png",
                     "assets/enemies/head_noel.png", [800, 300])
    noel_button = pygame.Rect((w - 300), (h - 300), 300, 300)
    noel_surf = pygame.Surface(noel_button.size)

    running = True
    start = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    infosBt = InfosBattle()
                    if clodo_button.collidepoint(event.pos):
                        if battle(surface, 0, gorille, clodo) == True:
                            lvl.append(0)
                    if titi_button.collidepoint(event.pos) and 0 in lvl:
                        if battle(surface, 1, gorille, titi) == True:
                            lvl.append(1)
                    if gaston_button.collidepoint(event.pos) and 1 in lvl:
                        if battle(surface, 2, gorille, gaston) == True:
                            lvl.append(2)
                    if ronald_button.collidepoint(event.pos) and 2 in lvl:
                        if battle(surface, 3, gorille, ronald) == True:
                            lvl.append(3)
                    if maman_button.collidepoint(event.pos) and 3 in lvl:
                        if battle(surface, 4, gorille, maman) == True:
                            lvl.append(4)
                    if noel_button.collidepoint(event.pos) and 4 in lvl:
                        if battle(surface, 5, gorille, noel) == True:
                            lvl.append(5)
        surface.fill((255, 255, 255))                   #BACK
        clodo.setLogoPos(10, 10)                        #CLODO
        titi.setLogoPos(((w - 300) / 2), 10)            #TITI
        gaston.setLogoPos((w - 300), 10)                #GASTON
        ronald.setLogoPos(10, (h - 300))                #RONALD
        maman.setLogoPos(((w - 300) / 2), (h - 300))    #MAMAN
        noel.setLogoPos((w - 300), (h - 300))           #NOEL
        surface.blit(clodo.headSprite, clodo.logorect)
        surface.blit(titi.headSprite, titi.logorect)
        surface.blit(gaston.headSprite, gaston.logorect)
        surface.blit(ronald.headSprite, ronald.logorect)
        surface.blit(maman.headSprite, maman.logorect)
        surface.blit(noel.headSprite, noel.logorect)
        pygame.display.flip()

def initMusic():
    pygame.mixer.music.load("assets/Music/main_theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

ITEMS = [
    "assets/gorilla/gorilla_cigarette.png",
    "assets/gorilla/gorilla_casquette.png",
    "assets/gorilla/gorilla_tie.png",
    "assets/gorilla/gorilla_burger.png",
    "assets/gorilla/gorilla_enfant.png",
    "assets/gorilla/gorilla_noel.png",
]

def nbUndiscover(listItems):
    count = 0
    for item in listItems:
        if item.rect.x != 0:
            count += 1
    return count

def perso_menu():
    w, h = pygame.display.get_surface().get_size()
    gorille = Character("assets/gorilla/gorilla_base.png",
                        "assets/gorilla/gorilla_base.png", [0, 0])
    
    gorille.setScale(700, 700)
    running = True

    listItems = []
    for i in lvl:
        item = Character(ITEMS[i], ITEMS[i], [0, 0])
        item.setScale(700, 700)
        listItems.append(item)
        item.setPosition(3000, 3000)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button.collidepoint(pygame.mouse.get_pos()):
                        for item in listItems:
                            if item.rect.x != 0:
                                item.setPosition(0, 0)
                                break
                    for item in listItems:
                        if item.getRect().collidepoint(event.pos):
                            if item.logorect.x == 0:
                                item.setPosition(3000, 3000)
                            else:
                                item.setPosition(0, 0)
        surface.fill((255, 255, 255))
        button = Button(surface, 800, 300, "? " + str(nbUndiscover(listItems)) + " objets disponibles ?")
        surface.blit(gorille.sprite, gorille.logorect)
        for item in listItems:
            surface.blit(item.sprite, item.logorect)
        pygame.display.flip()
    return

def initMenu():
    menu = pygame_menu.Menu('LA JOUTE', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', choose_menu)
    menu.add.button('Perso', perso_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    return menu

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    initMusic()
    menu = initMenu()

    menu.mainloop(surface)
