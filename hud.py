import pygame
from constantes import *
from auxiliar import Auxiliar

class HUD:
    def __init__(self, pantalla, personaje):
        self.pantalla = pantalla
        self.personaje = personaje
        self.img_barra_vida = pygame.image.load(PATH_IMAGE+"/hud/vida-0.png")
        self.rect_barra_vida = self.img_barra_vida.get_rect()
        self.img_barra_vida_kraken = None
        self.img_oxigeno = Auxiliar.personalizar_img(f"DEEP DIVE - SUBMARINE SOS/img/hud/oxygen.png", True, 40, 45, True, COLOR_NEGRO)
        self.rect_oxigeno = self.img_oxigeno.get_rect()
        self.rect_oxigeno.x = 840
        self.rect_oxigeno.y = 6
        self.img_submarino = Auxiliar.personalizar_img(f"DEEP DIVE - SUBMARINE SOS/img/botin/parte1.png", True, 40, 45, True, COLOR_ROJO_PAINT)
        self.rect_submarino = self.img_submarino.get_rect()
        self.rect_submarino.x = 710
        self.rect_submarino.y = 4
        self.img_misil = Auxiliar.personalizar_img(f"DEEP DIVE - SUBMARINE SOS/img/botin/misil.png", True, 40, 45, True, COLOR_BLANCO)
        self.rect_misil = self.img_misil.get_rect()
        self.rect_misil.x = 710
        self.rect_misil.y = 4
    def actualizar_hud(self,timer_segundos, kraken=None, nivel=None):
        vida = self.personaje.porcentaje_vida
        objetos = self.personaje.objetos
        if kraken:
            if kraken.vida != 0:
                self.img_barra_vida_kraken = Auxiliar.personalizar_img(f"DEEP DIVE - SUBMARINE SOS/img/hud/vida_kraken{kraken.vida}.png", True, 190, 40, True, COLOR_BLANCO)
                self.rect_vida_kraken = self.img_barra_vida_kraken.get_rect()
                self.rect_vida_kraken.x = 790
                self.rect_vida_kraken.y = 150
                self.pantalla.blit(self.img_barra_vida_kraken, self.rect_vida_kraken)
        self.img_barra_vida = Auxiliar.personalizar_img(f"{PATH_IMAGE}/hud/vida-{vida}.png", True, 180, 50, True, COLOR_ROJO_PAINT)


        #TODO poner la imagen del item a recoger según cada nivel
        font = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 30)
        color_fuente = COLOR_NEGRO
        texto = f"x{objetos}"
        text = font.render(texto, True, color_fuente)
        text_rect = text.get_rect()
        text_rect.x = 750  # Centrar en el eje X
        text_rect.y = 15  # Posicionar en el eje Y a 50
        if nivel:
            if nivel == "nivel_1":
                self.pantalla.blit(self.img_submarino, self.rect_submarino)
                self.pantalla.blit(text, text_rect)
            elif nivel == "nivel_2":
                self.pantalla.blit(self.img_misil, self.rect_misil)
                self.pantalla.blit(text, text_rect)
            elif nivel == "nivel_3":
                color_fuente = COLOR_BLANCO

        #texto temporizador oxigeno
        temporizador = f"={timer_segundos}"
        temporizador = font.render(temporizador, True, color_fuente)
        temporizador_rect = temporizador.get_rect()
        temporizador_rect.x = 880  # Centrar en el eje X
        temporizador_rect.y = 15  # Posicionar en el eje Y a 50
        self.pantalla.blit(temporizador, temporizador_rect)

        # Bliteo barra de vida e imagen oxígeno
        self.pantalla.blit(self.img_barra_vida, self.rect_barra_vida)
        self.pantalla.blit(self.img_oxigeno, self.rect_oxigeno)
