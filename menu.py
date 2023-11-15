import pygame
from constantes import *
from niveles import Nivel_1
from niveles import Nivel_2
from niveles import Nivel_3
from sonido import Sonido_y_musica
from pantallas import Pantallas
from auxiliar import Auxiliar

class Menu_inicio:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.keys = None
        self.eventos = None
        self.tiempo_transcurrido = 0
        self.nivel_1 = None
        self.nivel_2 = None
        self.nivel_3 = None
        self.background_menu = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/menu/background-lvl-2.jpg", True, 1000, ALTO_VENTANA)
        self.img_opciones = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/menu/opciones_menu.png", True, 400, 450)
        self.opciones = ["Nuevo Juego", "Opciones", "Score"]
        self.seleccionado = None
        self.correr = True
        self.blitear_menu = True
        self.sonido = Sonido_y_musica()
        self.tiempo_restante = 60
        self.evento_timer = pygame.USEREVENT
        pygame.time.set_timer(self.evento_timer, 1000)
        self.nuevo_nivel = False
        self.timer_reiniciado = False
        self.timer_reiniciado_1 = False
        self.timer_reiniciado_2 = False
        self.sacar_pantalla_muerte = False
        self.bandera_crear_instancia_1 = True
        self.bandera_crear_instancia_2 = True
        self.bandera_crear_instancia_3 = True
        self.pantalla_carga = Pantallas(self.pantalla)
        self.blitear_pantalla_nuevo_nivel_1 = True
        self.blitear_pantalla_nuevo_nivel_2 = True
        self.blitear_pantalla_nuevo_nivel_3 = True
        self.blitear_pantalla_inicio = True
        self.bandera_comienzo_nivel_1 = False


    def reinicio_de_etiquetas(self):
        self.keys = None
        self.eventos = None
        self.tiempo_transcurrido = 0
        self.nivel_1 = None
        self.nivel_2 = None
        self.nivel_3 = None
        self.background_menu = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/background-lvl-2.jpg").convert()
        self.background_menu = pygame.transform.scale(self.background_menu, (1000, ALTO_VENTANA))
        self.img_opciones = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/opciones_menu.png").convert()
        self.img_opciones = pygame.transform.scale(self.img_opciones, (400, 450))
        self.opciones = ["Nuevo Juego", "Opciones", "Score"]
        self.seleccionado = None
        self.correr = True
        self.blitear_menu = True
        self.sonido = Sonido_y_musica()
        self.tiempo_restante = 60
        self.evento_timer = pygame.USEREVENT
        pygame.time.set_timer(self.evento_timer, 1000)
        self.nuevo_nivel = False
        self.timer_reiniciado = False
        self.timer_reiniciado_1 = False
        self.timer_reiniciado_2 = False
        self.sacar_pantalla_muerte = False
        self.bandera_crear_instancia_1 = True
        self.bandera_crear_instancia_2 = True
        self.bandera_crear_instancia_3 = True
        self.pantalla_carga = Pantallas(self.pantalla)
        self.blitear_pantalla_nuevo_nivel_1 = True
        self.blitear_pantalla_nuevo_nivel_2 = True
        self.blitear_pantalla_nuevo_nivel_3 = True
        self.blitear_pantalla_inicio = True
        self.bandera_comienzo_nivel_1 = False
        #TODO agregar los nuevos atributos que vaya agregando


    def mostrar_menu(self, lista_eventos, tiempo_transcurrido):
        self.tiempo_transcurrido = tiempo_transcurrido
        self.eventos = lista_eventos
        self.manejar_eventos()
        if self.blitear_menu:
            self.pantalla.blit(self.background_menu, (0,0))
            self.pantalla.blit(self.img_opciones, (300, 0))
            self.img_opciones.set_colorkey(COLOR_ROJO_PAINT)
            self.sonido.volumen_menu = 0.5
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
                if self.blitear_menu:
                    if (pos_mous[0] >= 375 and pos_mous[0] <= 616) and (pos_mous[1] >= 172 and pos_mous[1] <= 239):
                        self.seleccionado = 0
                    elif (pos_mous[0] >= 375 and pos_mous[0] <= 616) and (pos_mous[1] >= 268 and pos_mous[1] <= 333):
                        self.seleccionado = 1
            if evento.type == self.evento_timer:
                if self.tiempo_restante > 0:
                    self.tiempo_restante -= 1
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_BACKSPACE:
                    if self.nivel_1:
                        self.nivel_1.blitear_pantalla_muerte = False
                        self.sonido.musica_fondo_lvl1.stop()
                    if self.nivel_2:
                        self.nivel_2.blitear_pantalla_muerte = False
                        self.sonido.musica_fondo_lvl2.stop()
                    elif self.nivel_3:
                        self.nivel_3.blitear_pantalla_muerte = False
                        self.sonido.musica_fondo_lvl3.stop()
                    self.blitear_menu = True
                    self.seleccionado = None
                    self.reinicio_de_etiquetas()
                if evento.key == pygame.K_RETURN:
                    if self.blitear_pantalla_inicio:
                        self.blitear_pantalla_inicio = False
                    elif self.bandera_comienzo_nivel_1:
                        self.blitear_pantalla_nuevo_nivel_1 = False
                    if self.nivel_1:
                        self.blitear_pantalla_nuevo_nivel_2 = False
                    if self.nivel_2:
                        self.blitear_pantalla_nuevo_nivel_3 = False
                #TODO lógica para pasar la pantalla de nuevo nivel y de las historias.

        if self.seleccionado is not None:
            self.keys = pygame.key.get_pressed()
            self.realizar_accion()

    def realizar_accion(self):
        if self.opciones[self.seleccionado] == "Nuevo Juego":
            self.blitear_menu = False
            if self.blitear_pantalla_inicio:
                self.pantalla_carga.pantalla_comienzo_historia()
                self.bandera_comienzo_nivel_1 = True
            elif self.blitear_pantalla_nuevo_nivel_1:
                self.pantalla_carga.nuevo_nivel("1")
            else:
                if self.bandera_crear_instancia_1:
                    self.nivel_1 = Nivel_1(self.pantalla)
                    self.bandera_crear_instancia_1 = False
                elif self.bandera_crear_instancia_1 == False and self.timer_reiniciado == False:
                    self.tiempo_restante = 60
                    self.timer_reiniciado = True
                self.nivel_1.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
                if self.nivel_1 and self.nivel_1.estado_nivel:
                    self.blitear_menu = False
                    if self.blitear_pantalla_nuevo_nivel_2:
                        self.pantalla_carga.nuevo_nivel("2")
                    else:
                        if self.bandera_crear_instancia_2:
                            self.nivel_2 = Nivel_2(self.pantalla)
                            self.bandera_crear_instancia_2 = False
                            if self.nivel_1.estado_nivel and self.timer_reiniciado_1 == False:
                                self.tiempo_restante = 60
                                self.timer_reiniciado_1 = True
                        self.nivel_2.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
                if self.nivel_2 and self.nivel_2.estado_nivel:
                    self.blitear_menu = False
                    if self.blitear_pantalla_nuevo_nivel_3:
                        self.pantalla_carga.nuevo_nivel("3")
                    else:
                        if self.bandera_crear_instancia_3:
                            self.nivel_3 = Nivel_3(self.pantalla)
                            self.bandera_crear_instancia_3 = False
                            if self.nivel_2.estado_nivel and self.timer_reiniciado_2 == False:
                                self.tiempo_restante = 60
                                self.timer_reiniciado_2 = True
                        self.nivel_3.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
                    #TODO armar una pantalla para preguntar si desea continuar en ese nivel
        elif self.opciones[self.seleccionado] == "Opciones":
            #TODO silenciar toda la música
            self.blitear_menu = False
            if self.bandera_crear_instancia_3:
                self.nivel_3 = Nivel_3(self.pantalla)
                self.bandera_crear_instancia_3 = False
            self.nivel_3.renderizar_nivel(self.keys, self.tiempo_transcurrido, self.tiempo_restante, self.sonido)
        elif self.opciones[self.seleccionado] == "Score":
            print("Ver puntuación")
            # lógica de puntuación
