import pygame
from constantes import *

class Pantallas():
    @staticmethod
    def pantalla_personaje_muerto(pantalla):#PANTALLA MENSAJE MUERTO
        fuente = pygame.font.SysFont("Arial Narrow", 50)
        texto = "Personaje muerto"
        text = fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 50  # Posicionar en el eje Y a 50
        pantalla.fill((COLOR_NEGRO)) #ponerle un fondo específico
        pantalla.blit(text, text_rect)
        
    @staticmethod
    def pantalla_fin_nivel(pantalla):#PANTALLA MENSAJE FIN NIVEL
        fuente = pygame.font.SysFont("Arial Narrow", 50)
        texto = "FIN DEL NIVEL 1"
        text = fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2  # Centrar en el eje X
        text_rect.y = 50  # Posicionar en el eje Y a 50
        pantalla.fill((COLOR_NEGRO)) #ponerle un fondo específico
        pantalla.blit(text, text_rect)
