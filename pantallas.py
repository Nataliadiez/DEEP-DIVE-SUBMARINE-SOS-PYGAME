import pygame
from constantes import *
from auxiliar import Auxiliar

class Pantallas():
    @staticmethod
    def personaje_muerto(pantalla):#PANTALLA MENSAJE MUERTO
        background = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/background/fondo_nivel.jpg", True, 1200, ALTO_VENTANA)
        fuente = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 50)
        texto = "Personaje muerto"
        text = fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 50  # Posicionar en el eje Y a 50
        pantalla.blit(background, (0,0))
        pantalla.blit(text, text_rect)
        

    @staticmethod
    def nuevo_nivel(pantalla):#PANTALLA MENSAJE MUERTO
        background = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/background/fondo_nivel.jpg", True, 1200, ALTO_VENTANA)
        fuente = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 50)
        texto = "Personaje muerto"
        text = fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 50  # Posicionar en el eje Y a 50
        pantalla.blit(background, (0,0))
        pantalla.blit(text, text_rect)
        
    @staticmethod
    def fin_nivel(pantalla):#PANTALLA MENSAJE FIN NIVEL
        background = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/background/fondo_nivel.jpg", True, 1200, ALTO_VENTANA)
        fuente = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 50)
        texto = "FIN DEL NIVEL 1"
        text = fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 50  # Posicionar en el eje Y a 50
        pantalla.blit(background, (0,0))
        pantalla.blit(text, text_rect)
