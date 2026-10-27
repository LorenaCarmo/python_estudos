# programa abre e reproduz mp3 

import pygame
pygame.init()
pygame.mixer.music.load('tocando_mp3_exerc_21.mp3')
pygame.mixer.music.play()
pygame.event.wait()

input('Tocando... aperte Enter para parar.')