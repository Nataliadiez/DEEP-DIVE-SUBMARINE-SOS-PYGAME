import pygame
from constantes import *
from auxiliar import Auxiliar


class Player:
    def __init__(self, x, y, velocidad):
        self.nadar_der = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/spritesheet-buzo-agua.png", 4, 4, 2, 170, 170)
        self.nadar_izq = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/spritesheet-buzo-agua.png", 4, 4, 1, 170, 170)
        self.nadar_arriba = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/spritesheet-buzo-agua.png", 4, 4, 3, 170, 170)
        self.nadar_abajo = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/spritesheet-buzo-agua.png", 4, 4, 0, 170, 170)
        self.posicion_x = x
        self.posicion_y = y
        self.velocidad = velocidad
        self.frame = 0
        self.vidas = 3
        self.porcentaje_vida = 60
        self.objetos = 0
        self.score = 0
        self.animation = self.nadar_der
        self.image = self.animation[self.frame]
        self.ancho_imagen = self.image.get_width()
        self.alto_imagen = self.image.get_height()
        self.img_pos_x = self.ancho_imagen
        self.vivo = True
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicion_x, self.posicion_y)

    def control(self, keys):
        self.posicion_x = 0
        self.posicion_y = 0

        if keys[pygame.K_RIGHT]:
            self.posicion_x = self.velocidad
            self.animation = self.nadar_der
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_LEFT]:
            self.posicion_x = -self.velocidad
            self.animation = self.nadar_izq
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_UP]:
            self.posicion_y = -self.velocidad
            self.animation = self.nadar_arriba
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_DOWN]:
            self.posicion_y = self.velocidad
            self.animation = self.nadar_abajo
            self.frame = (self.frame + 1) % len(self.animation)

    def update(self):
        x = self.rect.x + self.posicion_x
        y = self.rect.y + self.posicion_y
        if 0 <= x < ANCHO_VENTANA - self.ancho_imagen:
            self.rect.x = x
        if 240 <= y < ALTO_VENTANA - self.alto_imagen:
            self.rect.y = y


    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect.topleft)