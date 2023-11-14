import pygame
from constantes import *
from niveles import Nivel_1
from sonido import Sonido_y_musica
from niveles import Nivel_2
from niveles import Nivel_3

class Menu_inicio:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.keys = None
        self.eventos = None
        self.tiempo_transcurrido = 0
        self.nivel_1 = Nivel_1(self.pantalla)
        self.nivel_2 = Nivel_2(self.pantalla)
        self.nivel_3 = Nivel_3(self.pantalla)
        self.background_menu = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/background-lvl-2.jpg").convert()
        self.background_menu = pygame.transform.scale(self.background_menu, (1000, ALTO_VENTANA))
        self.img_opciones = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/opciones_menu.png").convert()
        self.img_opciones = pygame.transform.scale(self.img_opciones, (400, 450))
        self.opciones = ["Nuevo Juego", "Continuar", "Opciones", "Score"]
        self.seleccionado = None
        self.correr = True
        self.blitear_menu = True
        self.sonido = Sonido_y_musica()
        #TODO lógica para llevarme de acá a otra clase
        self.tiempo_restante = 60
        self.evento_timer = pygame.USEREVENT
        pygame.time.set_timer(self.evento_timer, 1000)
        self.nuevo_nivel = False
        self.timer_reiniciado_1 = False
        self.timer_reiniciado_2 = False

        """ self.tiempo_restante_2 = 60
        self.evento_timer_2 = pygame.USEREVENT + 1
        pygame.time.set_timer(self.evento_timer_2, 1000) """
        
    def mostrar_menu(self, lista_eventos, tiempo_transcurrido):
        if self.nivel_1.estado_nivel and self.timer_reiniciado_1 == False:
            self.tiempo_restante = 60
            self.timer_reiniciado_1 = True
        elif self.nivel_2.estado_nivel and self.timer_reiniciado_2 == False:
            self.tiempo_restante = 60
            self.timer_reiniciado_2 = True
        self.tiempo_transcurrido = tiempo_transcurrido
        self.eventos = lista_eventos
        self.manejar_eventos()
        if self.blitear_menu:
            self.pantalla.blit(self.background_menu, (0,0))
            self.pantalla.blit(self.img_opciones, (300, 0))
            self.img_opciones.set_colorkey(COLOR_ROJO_PAINT)
            self.sonido.volumen_menu = 0.2
            self.sonido.musica_fondo_menu.set_volume(self.sonido.volumen_menu)
        else:
            self.sonido.musica_fondo_menu.stop()
        return self.correr

    def manejar_eventos(self):
        for evento in self.eventos:
            #evento para cerrar la ventana
            if evento.type == pygame.QUIT or (evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE):
                self.correr = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos_mous = list(pygame.mouse.get_pos())
                print(pos_mous)
                if (pos_mous[0] >= 375 and pos_mous[0] <= 616) and (pos_mous[1] >= 172 and pos_mous[1] <= 239):
                    self.seleccionado = 0
                elif (pos_mous[0] >= 375 and pos_mous[0] <= 616) and (pos_mous[1] >= 268 and pos_mous[1] <= 333):
                    self.seleccionado = 1
            if evento.type == self.evento_timer:
                if self.tiempo_restante > 0:
                    self.tiempo_restante -= 1

        if self.seleccionado is not None:
            self.keys = pygame.key.get_pressed()
            self.realizar_accion()

    def realizar_accion(self):
        if self.opciones[self.seleccionado] == "Nuevo Juego":
            self.blitear_menu = False
            #TODO en la clase niveles, o en una nueva que se llama jugar, desde ahí llamar a los niveles
            self.nivel_1.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
            if self.nivel_1.estado_nivel:
                self.nivel_2.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
            if self.nivel_2.estado_nivel:
                self.nivel_3.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
            else:
                pass
                #TODO armar una pantalla para preguntar si desea continuar en ese nivel
        elif self.opciones[self.seleccionado] == "Continuar":
            self.blitear_menu = False
            self.nivel_3.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
        elif self.opciones[self.seleccionado] == "Opciones":
            print("Ir a opciones")
            # logica para silenciar la música
        elif self.opciones[self.seleccionado] == "Score":
            print("Ver puntuación")
            # lógica de puntuación
