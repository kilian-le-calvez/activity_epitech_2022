#!/usr/bin/env python
import pygame
import pygame_gui
from pygame_gui.windows.ui_file_dialog import UIFileDialog
from pygame_gui.elements.ui_button import UIButton
from pygame_gui.elements.ui_label import UILabel
import os
from pygame.rect import Rect
from pygame import display,movie

import moviepy.editor
import moviepy.video.fx.all
from moviepy.editor import VideoFileClip

from mp4_to_gif import Decoupeur as dec

pygame.init()

window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()

file_selection_button = UIButton(relative_rect=Rect(100, 200, 200, 100),
                                 manager=manager, text='Select File')

gif_gen_button = UIButton(relative_rect=Rect(500, 200, 200, 100),
            manager=manager, text='Generate gif')

play_gif_button = UIButton(relative_rect=Rect(300, 200, 200, 100),
            manager=manager, text='Play gif')

def loadingTextCreate(text):
    return UILabel(relative_rect=Rect(300, 300, 200, 100),
                                 manager=manager, text=text)

name_last_gif = ""

def playGif(path, window_surface):
    pygame.display.set_caption(path)
    clip = VideoFileClip(path)
    clip.preview()
    window_surface = pygame.display.set_mode((800, 600))

while 1:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == file_selection_button:
                    file_selection = UIFileDialog(rect=Rect(0, 0, 300, 300), manager=manager, allow_picking_directories=True)

                if event.ui_element == gif_gen_button:
                    text_loading = loadingTextCreate("Generating gif...")
                    manager.update(time_delta)
                    window_surface.blit(background, (0, 0))
                    manager.draw_ui(window_surface)
                    pygame.display.update()
                    decoupeur.createImages()
                    name_last_gif = decoupeur.make_gif("myGif")
                    text_loading.kill()

                if event.ui_element == play_gif_button:
                    playGif(name_last_gif, window_surface)
                    
                if event.ui_element == file_selection.ok_button:
                    text_loading = loadingTextCreate("Loading ressources...")
                    file_selection.kill()
                    manager.update(time_delta)
                    window_surface.blit(background, (0, 0))
                    manager.draw_ui(window_surface)
                    pygame.display.update()
                    
                    decoupeur = dec(str(file_selection.current_file_path))
                    decoupeur.loadVideo()
                    text_loading.kill()

        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()