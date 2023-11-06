import pygame
import sys
from constantes import *
from player import Player
from enemigo import *
from background import *
from hud import *
from mensajes_pantalla import *
from botin import *

pygame.init()
#pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA , ALTO_VENTANA))
titulo_ventana = pygame.display.set_caption("Prueba con pygame")
CLOCK = pygame.time.Clock()

#background 
background = Background("DEEP DIVE - SUBMARINE SOS/img/background/ecco3.png")

#logica scroll
lvl_pos_x = 0

#personaje
buzo = Player(50, LIMITE_AGUA, 5)

#creación de tiburones 
tiburon = Tiburon(2000, 200, 80, 40)
tiburon2 = Tiburon(1500, 350, 80, 40)
tiburon3 = Tiburon(1500, 500, 100, 60)

# Crear una instancia de HUD
hud = HUD(pantalla, buzo)

botin = Botin(background.background_pos_x-2000, ALTO_VENTANA-100)

botin1 = Botin(background.background_pos_x-4000, LIMITE_AGUA+20)

botin2 = Botin(background.background_pos_x-200, 300)


#TIMER cosas que van a pasar con una cadencia, por ejemplo mover enemigos
clock = pygame.time.Clock()

correr = True
while correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        # Evento para cerrar la ventana
        if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
            correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            pos_mous = pygame.mouse.get_pos()
            print(pos_mous)
            #print(background.image.get_width())

    #captura los eventos de teclas presionadas
    keys = pygame.key.get_pressed()

    # Eventos de teclado
    buzo.control(keys)

    # Cálculo del movimiento del fondo basado en la posición del jugador
    x_relativa = lvl_pos_x % background.ancho
    if buzo.vivo:
        lvl_pos_x = background.scroll_background(buzo, tiburon, tiburon2, tiburon3, lvl_pos_x)
    background_pos_x = x_relativa

    pantalla.fill((0, 0, 0))
    background.draw(pantalla, background_pos_x)

    if buzo.vivo:
        botin.esparcir_botin(buzo, pantalla, background_pos_x-botin.rect.width)
        botin1.esparcir_botin(buzo, pantalla, background_pos_x-botin.rect.width)
        botin2.esparcir_botin(buzo, pantalla, background_pos_x-botin.rect.width)
        tiburon.update()
        tiburon2.update()
        tiburon3.update()
        tiburon.draw(pantalla, buzo)
        tiburon2.draw(pantalla, buzo)
        tiburon3.draw(pantalla, buzo)
        buzo.update()
        buzo.draw(pantalla)
        
        
        #pygame.draw.rect(pantalla, COLOR_ROJO, background_rect, 1) rect del background
        hud.actualizar_hud()
        #delta_ms = clock.tick(FPS) #cuantos mili pasaron desde la última vez
        """ if buzo.objetos >= 5:
            pantalla_fin_nivel(pantalla) """
    else:
        pantalla_personaje_muerto(pantalla)

    pygame.display.flip()
    CLOCK.tick(FPS)

pygame.quit()
sys.exit()
