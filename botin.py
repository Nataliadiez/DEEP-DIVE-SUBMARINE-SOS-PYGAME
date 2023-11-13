import pygame
from constantes import *
from auxiliar import *
import random

class Botin():
    def __init__(self, pos_x, pos_y) -> None:
        opciones_botin = [
            PATH_IMAGE+"/botin/parte1.png",
            PATH_IMAGE+"/botin/parte2.png",
            PATH_IMAGE+"/botin/parte3.png"
        ]
        imagen_elegida = random.choice(opciones_botin)
        self.objeto = pygame.image.load(imagen_elegida)
        self.objeto = pygame.transform.scale(self.objeto, (50, 60))
        self.rect = self.objeto.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.original_x = pos_x  # Guardar la posición original en relación al fondo
        self.original_y = pos_y
        self.visible = True
        self.colision_botin = True
        
    #Esta lógica me sirve para poder hacer que recoja los elementos del submarino
    def esparcir_botin(self, pantalla, scroll_amount_x):
        if self.visible:
            # Actualiza la posición del botín con el scroll_amount en ambos ejes
            self.rect.x = self.original_x + scroll_amount_x
            self.objeto.set_colorkey(COLOR_ROJO_PAINT)
            pantalla.blit(self.objeto, self.rect)


class Armas(Botin):
    def __init__(self, pos_x, pos_y) -> None:
        super().__init__(pos_x, pos_y)
        opciones_botin = [
            PATH_IMAGE+"/botin/arma1.png",
            PATH_IMAGE+"/botin/arma2.png",
            PATH_IMAGE+"/botin/arma3.png"
        ]
        imagen_elegida = random.choice(opciones_botin)
        self.objeto = pygame.image.load(imagen_elegida)
        self.objeto = pygame.transform.scale(self.objeto, (60, 40))
        self.rect = self.objeto.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.original_x = pos_x  # Guardar la posición original en relación al fondo
        self.original_y = pos_y
        self.visible = True
        self.colision_botin = True
        
    #Esta lógica me sirve para poder hacer que recoja los elementos del submarino
    def esparcir_botin(self, pantalla, scroll_amount_x):
        if self.visible:
            # Actualiza la posición del botín con el scroll_amount en ambos ejes
            self.rect.x = self.original_x + scroll_amount_x
            self.objeto.set_colorkey(COLOR_BLANCO)
            pantalla.blit(self.objeto, self.rect)