import pygame
from constantes import *
import random


class Tiburon:
    def __init__(self, x, y, ancho, alto):
        self.imagen = pygame.image.load(PATH_IMAGE+"/Shark1.png")
        self.imagen = pygame.transform.scale(self.imagen, (ancho, alto))
        self.rect_imagen = self.imagen.get_rect()
        self.rect_imagen.x = random.randrange(200, 2000, 100)
        self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 100)
        self.visible = True
        self.velocidad = random.randrange(2, 8, 1)
        self.lista_tiburones = []
    
    def update(self):
        self.rect_imagen.x -= self.velocidad

    def draw(self, pantalla, personaje):
        if self.visible and personaje.rect.colliderect(self.rect_imagen):
            personaje.porcentaje_vida -= 10
            self.visible = False
        if personaje.porcentaje_vida <= 0:
            personaje.vivo = False
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, 600, 130)
            self.visible = True 
