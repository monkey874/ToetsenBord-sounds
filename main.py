import keyboard
import pygame
import os

import fileLoader

loader = fileLoader.loader(4, '.mp3')
test = loader.LoadFile()

pygame.mixer.init()
pygame.mixer.music.load(test[0])
def play(key):
    print(f"Key pressed: {key.name}")
    pygame.mixer.music.play()

keyboard.on_press(play)
keyboard.wait('esc') 
