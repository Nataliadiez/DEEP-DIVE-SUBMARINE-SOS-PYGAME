import pygame
from constantes import *
from botin import *

class Background:
    def __init__(self, image_path, ancho=None, alto=None, scale=False):
        self.image = pygame.image.load(image_path).convert()
        if scale:
            self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.ancho = self.image.get_rect().width
        self.alto = self.image.get_rect().height
        self.pos_x = 0
        self.background_pos_x = 0 #para luego llamar desde niveles a esta variable y pasarsela a la clase botin

    def draw(self, screen, background_pos_x):
        self.background_pos_x = background_pos_x
        screen.blit(self.image, (background_pos_x - self.ancho, 0))
        if background_pos_x < ANCHO_VENTANA:
            screen.blit(self.image, (background_pos_x, 0))


    @staticmethod        
    def scroll_background(buzo, lista_tiburones, lvl_pos_x):
        if buzo.rect.centerx > ANCHO_MITAD_VENTANA and buzo.posicion_x > 0:
            buzo.posicion_x -= buzo.velocidad
            lvl_pos_x -= 5
            for tiburon in lista_tiburones:
                tiburon.rect_imagen.x -= 5

        if buzo.rect.centerx < ANCHO_MITAD_VENTANA and buzo.posicion_x < 0:
            buzo.posicion_x += buzo.velocidad
            lvl_pos_x += 5
            for tiburon in lista_tiburones:
                tiburon.rect_imagen.x += 5
        return lvl_pos_x


class StaticBackground(Background):
    def __init__(self, image_path, ancho=None, alto=None, scale=False):
        super().__init__(image_path, ancho, alto, scale)
    
    def draw(self, screen):
        screen.blit(self.image, (0, 0))

    @staticmethod
    def scroll_background(buzo, lista_tiburones, lvl_pos_x):
        return lvl_pos_x
    