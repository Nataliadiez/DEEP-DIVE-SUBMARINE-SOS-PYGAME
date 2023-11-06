import pygame
from constantes import *
import random
from botin import *

class Background:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path).convert()
        self.ancho = self.image.get_rect().width
        self.pos_x = 0
        self.background_pos_x = 0 #para luego llamar desde main a esta variable y pasarsela a la clase botin
        # Lista de botines

    """ def update_position(self):
        # Generar botines al azar
        if random.randint(0, 1000) < 10:  # Puedes ajustar la probabilidad
            botin = Botin(self.background_pos_x, 200)  # Crear una instancia de Botin
            self.botines.append(botin)  # Agregar el botín a la lista """

    def draw(self, screen, background_pos_x):
        self.background_pos_x = background_pos_x
        screen.blit(self.image, (background_pos_x - self.ancho, 0))
        if background_pos_x < ANCHO_VENTANA:
            screen.blit(self.image, (background_pos_x, 0))


    @staticmethod        
    def scroll_background(buzo, tiburon, tiburon2, tiburon3, lvl_pos_x):
            if buzo.rect.centerx > ANCHO_MITAD_VENTANA and buzo.posicion_x > 0:
                buzo.posicion_x -= buzo.velocidad
                lvl_pos_x -= 5
                tiburon.rect_imagen.x -= 5
                tiburon2.rect_imagen.x -= 5
                tiburon3.rect_imagen.x -= 5

            if buzo.rect.centerx < ANCHO_MITAD_VENTANA and buzo.posicion_x < 0:
                buzo.posicion_x += buzo.velocidad
                lvl_pos_x += 5
                tiburon.rect_imagen.x += 5
                tiburon2.rect_imagen.x += 5
                tiburon3.rect_imagen.x += 5
            return lvl_pos_x