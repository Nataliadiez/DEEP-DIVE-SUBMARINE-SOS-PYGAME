import pygame
import sys
from constantes import *
from niveles import Niveles

class Menu_inicio:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.keys = None
        self.eventos = None
        self.tiempo_transcurrido = 0
        self.niveles = Niveles(self.pantalla)
        self.background_menu = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/background-lvl-2.jpg").convert()
        self.background_menu = pygame.transform.scale(self.background_menu, (1000, ALTO_VENTANA))
        self.img_opciones = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/opciones_menu.png").convert()
        self.img_opciones = pygame.transform.scale(self.img_opciones, (850, 550))
        self.opciones = ["Nuevo Juego", "Continuar", "Opciones", "Score"]
        self.seleccionado = None
        self.correr = True
        self.blitear_menu = True
        #TODO lógica para llevarme de acá a otra clase
        self.tiempo_restante = 60
        self.evento_timer = pygame.USEREVENT
        pygame.time.set_timer(self.evento_timer, 1000)
        

    def mostrar_menu(self, lista_eventos, tiempo_transcurrido):
        self.eventos = lista_eventos
        self.tiempo_transcurrido = tiempo_transcurrido
        self.manejar_eventos()
        if self.blitear_menu:
            self.pantalla.blit(self.background_menu, (0,0))
            self.pantalla.blit(self.img_opciones, (-40,-40))
            self.img_opciones.set_colorkey(COLOR_BLANCO)
        
        return self.correr
        

    def manejar_eventos(self):
        for evento in self.eventos:
            #evento para cerrar la ventana
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                self.correr = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mous = list(pygame.mouse.get_pos())
                print(pos_mous)
                if (pos_mous[0] >= 259 and pos_mous[0] <= 480) and (pos_mous[1] >= 197 and pos_mous[1] <= 264):
                    self.seleccionado = 0
            if evento.type == self.evento_timer:
                if self.tiempo_restante > 0:
                    self.tiempo_restante -= 1
                    

        if self.seleccionado is not None:
            self.keys = pygame.key.get_pressed()
            self.realizar_accion()

    def realizar_accion(self):
        if self.opciones[self.seleccionado] == "Nuevo Juego":
            self.blitear_menu = False
            self.niveles.nivel_1(self.keys, self.tiempo_transcurrido, self.tiempo_restante)
        elif self.opciones[self.seleccionado] == "Continuar":
            print("Continuar juego")
            # logica para continuar con el nivel en que estaba jugando
        elif self.opciones[self.seleccionado] == "Opciones":
            print("Ir a opciones")
            # logica para silenciar la música
        elif self.opciones[self.seleccionado] == "Score":
            print("Ver puntuación")
            # lógica de puntuación
