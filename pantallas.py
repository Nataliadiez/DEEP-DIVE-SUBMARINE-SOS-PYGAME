import pygame
from constantes import *
from auxiliar import Auxiliar

class Pantallas():
    def __init__(self, pantalla) -> None:
        self.pantalla = pantalla
        self.fuente = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 50)
        self.fuente_texto_largo = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 20)
        self.fuente_texto_muy_largo = pygame.font.Font("DEEP DIVE - SUBMARINE SOS/fonts/ARCADE_N.TTF", 15)
        self.background_cargas = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/background/fondo_nivel.jpg", True, 1200, ALTO_VENTANA)
        self.background_cargas_extra = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/background/fondo_nivel.jpg", True, 1200, ALTO_VENTANA)
        self.img_teclas = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/menu/teclas.png", True, 200,110, True, COLOR_ROJO_PAINT)
        self.img_spacebar = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/menu/spacebar.png", True, 200,80,True, COLOR_ROJO_PAINT)
        

    #TODO muerte del player
    def personaje_muerto(self):
        texto = "Personaje muerto"
        text = self.fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)
    
    #TODO nuevo nivel
    def nuevo_nivel(self, nivel):
        texto = f"NIVEL {nivel}"
        text = self.fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)

    #TODO para el final del nivel 3 con el kraken
    def pantalla_fin_juego(self):
        texto = "Felicidades! Has completado la mision."
        texto_2 = "Los tripulantes del Titan de Ocean Gate"
        texto_3 = "han regresado con sus familias"
        texto_4 = "gracias a tu valiente rescate."
        texto_5 = "Presione backspace para volver al menu."
        text = self.fuente_texto_largo.render(texto, True, COLOR_BLANCO)
        text_2 = self.fuente_texto_largo.render(texto_2, True, COLOR_BLANCO)
        text_3 = self.fuente_texto_largo.render(texto_3, True, COLOR_BLANCO)
        text_4 = self.fuente_texto_largo.render(texto_4, True, COLOR_BLANCO)
        text_5 = self.fuente_texto_largo.render(texto_5, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect_2 = text_2.get_rect()
        text_rect_3 = text_3.get_rect()
        text_rect_4 = text_4.get_rect()
        text_rect_5 = text_5.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect_2.centerx = ANCHO_VENTANA // 2
        text_rect_3.centerx = ANCHO_VENTANA // 2
        text_rect_4.centerx = ANCHO_VENTANA // 2
        text_rect_5.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        text_rect_2.y = 100
        text_rect_3.y = 150
        text_rect_4.y = 200
        text_rect_5.y = 350
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)
        self.pantalla.blit(text_2, text_rect_2)
        self.pantalla.blit(text_3, text_rect_3)
        self.pantalla.blit(text_4, text_rect_4)
        self.pantalla.blit(text_5, text_rect_5)

    #TODO cuando haces click en score en el menú de inicio, que te muestre el score
    def pantalla_score(self):
        texto = "SCORE"
        text = self.fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)

    #TODO pantalla mostrando la historia del rescate del submarino
    def pantalla_comienzo_historia(self):
        texto = "Hace 30 minutos, el submarino Titan de la empresa Ocean Gate"
        texto_2 = "perdio toda comunicacion con la base."
        texto_3 = "Desesperadas, las familias de los pasajeros a bordo han contratado"
        texto_4 = "tus habilidades como buzo experto para llevar a cabo el rescate."
        texto_5 = "Adentrate en las profundidades submarinas y salva a quienes"
        texto_6 = "estan atrapados antes de que se pierdan para siempre."
        text = self.fuente_texto_muy_largo.render(texto, True, COLOR_BLANCO)
        text_2 = self.fuente_texto_muy_largo.render(texto_2, True, COLOR_BLANCO)
        text_3 = self.fuente_texto_muy_largo.render(texto_3, True, COLOR_BLANCO)
        text_4= self.fuente_texto_muy_largo.render(texto_4, True, COLOR_BLANCO)
        text_5 = self.fuente_texto_muy_largo.render(texto_5, True, COLOR_BLANCO)
        text_6 = self.fuente_texto_muy_largo.render(texto_6, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect_2 = text_2.get_rect()
        text_rect_3 = text_3.get_rect()
        text_rect_4 = text_4.get_rect()
        text_rect_5 = text_5.get_rect()
        text_rect_6 = text_6.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect_2.centerx = ANCHO_VENTANA // 2
        text_rect_3.centerx = ANCHO_VENTANA // 2
        text_rect_4.centerx = ANCHO_VENTANA // 2
        text_rect_5.centerx = ANCHO_VENTANA // 2
        text_rect_6.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        text_rect_2.y = 100
        text_rect_3.y = 150
        text_rect_4.y = 200
        text_rect_5.y = 250
        text_rect_6.y = 300
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)
        self.pantalla.blit(text_2, text_rect_2)
        self.pantalla.blit(text_3, text_rect_3)
        self.pantalla.blit(text_4, text_rect_4)
        self.pantalla.blit(text_5, text_rect_5)
        self.pantalla.blit(text_6, text_rect_6)
        self.pantalla.blit(self.img_teclas, (293, 380))
        self.pantalla.blit(self.img_spacebar, (708, 400))
        
    def pantalla_uso_teclas(self):
        texto = "FIN DEL NIVEL 1"
        text = self.fuente.render(texto, True, COLOR_BLANCO)
        text_rect = text.get_rect()
        text_rect.centerx = ANCHO_VENTANA // 2
        text_rect.y = 50
        self.pantalla.blit(self.background_cargas, (0,0))
        self.pantalla.blit(text, text_rect)
