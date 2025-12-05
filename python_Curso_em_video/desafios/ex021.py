#import pygame
#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play()
#pygame.event.wait()              
     
     
import pygame
import time

pygame.init()
pygame.mixer.init()  # Inicializa o mixer de áudio

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()

# Espera enquanto a música estiver tocando
while pygame.mixer.music.get_busy():
    time.sleep(1)
     