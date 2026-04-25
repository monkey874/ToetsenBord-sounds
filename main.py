import keyboard
import pygame

pygame.mixer.init()
pygame.mixer.music.load('sound.mp3')

def play(key):
    print(f"Key pressed: {key.name}")
    pygame.mixer.music.play()

keyboard.on_press(play)
keyboard.wait('esc') 