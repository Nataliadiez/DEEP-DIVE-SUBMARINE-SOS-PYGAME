import pygame
from constantes import *
from auxiliar import *
import random

class Burbujas():
    def __init__(self, pos_x, pos_y) -> None:
        #self.objeto = pygame.image.load(imagen_elegida)
        self.objeto = pygame.transform.scale(self.objeto, (25, 30))
        self.rect = self.objeto.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.original_x = pos_x  # Guardar la posición original en relación al fondo
        self.original_y = pos_y
        self.visible = True
        
    #Esta lógica me sirve para poder hacer que recoja los elementos del submarino
    def esparcir_botin(self, personaje, pantalla, scroll_amount_x):
        if personaje.rect.colliderect(self.rect):
            self.visible = False
            personaje.objetos += 1
        if self.visible:
            # Actualiza la posición del botín con el scroll_amount en ambos ejes
            self.rect.x = self.original_x + scroll_amount_x
            self.objeto.set_colorkey(COLOR_ROJO_PAINT)
            pantalla.blit(self.objeto, self.rect)