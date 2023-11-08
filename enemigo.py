import pygame
from constantes import *
import random
from auxiliar import Auxiliar


class Tiburon:
    def __init__(self, ancho, alto):
        self.nadar_izq = Auxiliar.getSurfaceFromSprite(f"{PATH_IMAGE}\Shark-Sheet.png",8,1,0, ancho, alto)
        self.visible = True
        self.velocidad = random.randrange(2, 8, 1) #velocidad
        self.lista_tiburones = []
        self.animation = self.nadar_izq
        self.frame = 0
        self.imagen = self.animation[self.frame]
        self.rect_imagen = self.imagen.get_rect()
        self.rect_imagen.x = random.randrange(200, 2000, 100) #donde aparecen eje x
        self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 100) #donde aparecen eje y
        self.rect_colision = (self.rect_imagen.x ,self.rect_imagen.y ,100,80)
        
    def mover_tiburones(self):
        self.animation = self.nadar_izq
        self.frame = (self.frame + 1) % len(self.animation)

    def update(self):
        self.rect_imagen.x -= self.velocidad

    def draw(self, pantalla, personaje):
        self.image = self.animation[self.frame]
        self.rect_colision = (self.rect_imagen.x ,self.rect_imagen.y+30 ,30,20)
        
        if self.visible and personaje.rect.colliderect(self.rect_colision):
            personaje.porcentaje_vida -= 10
            self.visible = False
        if personaje.porcentaje_vida <= 0:
            personaje.vivo = False
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 130)
            self.visible = True 
