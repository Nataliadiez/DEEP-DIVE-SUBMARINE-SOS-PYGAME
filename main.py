import pygame
import sys
from constantes import *
from menu import *

pygame.init()

#pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA , ALTO_VENTANA))
titulo_ventana = pygame.display.set_caption("DEEP DIVE - SUBMARINE SOS")
CLOCK = pygame.time.Clock()

menu = Menu_inicio(pantalla)
for i in range (len(menu.nivel_1.lista_tiburones)):
    tiburon = menu.nivel_1.lista_tiburones
    if i <= 2:
        tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/Shark-Sheet.png", 8, 1, 0, ANCHO_TIBURON,ALTO_TIBURON, False, None)
    else:
        tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/pez_espada.png", 4, 1, 0, 300, 50, False, None)


while menu.correr:
    lista_eventos = pygame.event.get()
    tiempo_transcurrido = CLOCK.tick(FPS)
    CLOCK.tick(FPS) # Obtener el tiempo transcurrido
    menu.mostrar_menu(lista_eventos, tiempo_transcurrido)
    pygame.display.flip()

pygame.quit()
sys.exit()
