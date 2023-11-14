import pygame
import sys
from constantes import *
from menu import *
from auxiliar import Auxiliar

pygame.init()

#pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA , ALTO_VENTANA))
titulo_ventana = pygame.display.set_caption("DEEP DIVE - SUBMARINE SOS")
CLOCK = pygame.time.Clock()

menu = Menu_inicio(pantalla)

while menu.correr:
    lista_eventos = pygame.event.get()
    tiempo_transcurrido = CLOCK.tick(FPS)# Obtener el tiempo transcurrido
    menu.mostrar_menu(lista_eventos, tiempo_transcurrido)
    pygame.display.flip()
pygame.quit()
sys.exit()
