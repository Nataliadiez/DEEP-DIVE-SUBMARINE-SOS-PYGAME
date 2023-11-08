import pygame
import sys
from constantes import *
from niveles import *

pygame.init()

#pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA , ALTO_VENTANA))
titulo_ventana = pygame.display.set_caption("Prueba con pygame")
CLOCK = pygame.time.Clock()

niveles = Niveles(pantalla)

correr = True
while correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        # Evento para cerrar la ventana
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mous = pygame.mouse.get_pos()
            #print(pos_mous)
    #captura los eventos de teclas presionadas
    keys = pygame.key.get_pressed()
    tiempo_transcurrido = CLOCK.tick(FPS)  # Obtener el tiempo transcurrido
    niveles.nivel_1(keys, tiempo_transcurrido)
    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
