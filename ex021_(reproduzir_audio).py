'''import pygame
pygame.init()
pygame.mixer.music.load('despedida.mp3')
pygame.mixer.music.play()
a = 'começou'
while a != 'fim':
    a = input('Digite algo')
    if a == 'parar':
        pygame.mixer.music.stop()
    elif a == 'começar':
        pygame.mixer.music.play()
    elif a == 'pausar':
        pygame.mixer.music.pause()
    elif a == 'voltar':
        pygame.mixer.music.unpause()
    elif a == 'finalizar':
        pygame.mixer.music.fadeout(5000)
    elif a == 'posicao':
        print(pygame.mixer.music.get_pos())
'''

import pygame
pygame.init()
pygame.mixer.music.load('despedida.mp3')
pygame.mixer.music.play()
parada = input('Digite qualquer coisa para parar a música: ')