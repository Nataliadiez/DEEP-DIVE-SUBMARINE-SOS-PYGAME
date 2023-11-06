import pygame
from constantes import *

class HUD:
    def __init__(self, pantalla, personaje):
        self.pantalla = pantalla
        self.personaje = personaje
        self.img_barra_vida = pygame.image.load(PATH_IMAGE+"/hud/vida-0.png")
        self.rect_barra_vida = self.img_barra_vida.get_rect()
        

    def actualizar_hud(self):
        vida = self.personaje.porcentaje_vida
        objetos = self.personaje.objetos
        self.img_barra_vida = pygame.image.load(f"{PATH_IMAGE}/hud/vida-{vida}.png")
        self.img_barra_vida = pygame.transform.scale(self.img_barra_vida, (180,50))
        self.img_barra_vida.set_colorkey(COLOR_ROJO_PAINT)

        pantalla_ancho = ANCHO_VENTANA
        pantalla_altura = ALTO_VENTANA

        #PANTALLA MENSAJE MUERTO
        font = pygame.font.SysFont("Arial Narrow", 50)
        texto = str(objetos)
        text = font.render(texto, True, COLOR_NEGRO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 15  # Posicionar en el eje Y a 50
        


        # Dibujar el texto en la pantalla
        self.pantalla.blit(self.img_barra_vida, (self.rect_barra_vida))
        self.pantalla.blit(text, text_rect)
