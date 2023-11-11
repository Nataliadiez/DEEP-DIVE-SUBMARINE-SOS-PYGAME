import pygame
from constantes import *
import random
from auxiliar import Auxiliar


class Tiburon:
    def __init__(self):
        self.nadar_izq = Auxiliar.getSurfaceFromSprite(f"{PATH_IMAGE}/enemigos/Shark-Sheet.png",8,1,0, ANCHO_TIBURON, ALTO_TIBURON)
        self.velocidad = random.randrange(3, 10, 1) #velocidad
        self.lista_tiburones = []
        self.animation = self.nadar_izq
        self.frame = 0
        self.imagen = self.animation[self.frame]
        self.rect_imagen = self.imagen.get_rect()
        self.rect_imagen.x = random.randrange(600, 2000, 100) #donde aparecen eje x
        self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 100) #donde aparecen eje y
        self.rect_colision = (self.rect_imagen.x ,self.rect_imagen.y,100,80)
        self.tiempo_transcurrido = 0
        self.tiempo_cambio_frame = 200  # Tiempo (en milisegundos) para cambiar de frame
        self.colision_tiburon = True
        

    def update(self, delta_tiempo):
        # Incrementar el tiempo transcurrido
        self.tiempo_transcurrido += delta_tiempo
        # Cambiar de frame si ha pasado el tiempo necesario
        if self.tiempo_transcurrido >= self.tiempo_cambio_frame:
            self.frame = (self.frame + 1) % len(self.animation)
            self.imagen = self.animation[self.frame]
            self.tiempo_transcurrido = 0  # Reiniciar el contador
            
        self.rect_colision = (self.rect_imagen.x, self.rect_imagen.y + 20, 50, 30)
        self.rect_imagen.x -= self.velocidad

    def draw(self, pantalla):
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 130)
            self.colision_tiburon = True
