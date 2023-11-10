import pygame
from constantes import *
from background import *
from enemigo import *
from player import *
from hud import *
from pantallas import Pantallas

class Niveles:
    def __init__(self, pantalla) -> None:
        self.background = Background("DEEP DIVE - SUBMARINE SOS/img/background/ecco3.png")#background
        self.lvl_pos_x = 0 #logica scroll
        self.buzo = Player(50, LIMITE_AGUA, 5)#personaje
        self.tiburon1 = Tiburon(800, 85)#creación de tiburones
        self.tiburon2 = Tiburon(800, 85)#creación de tiburones
        self.tiburon3 = Tiburon(800, 85)#creación de tiburones
        self.botin1 = Botin(self.background.background_pos_x-2000, LIMITE_AGUA+50)
        self.botin2 = Botin(self.background.background_pos_x-4000, LIMITE_AGUA+200)
        self.botin3 = Botin(self.background.background_pos_x-6000, LIMITE_AGUA+20)
        self.botin4 = Botin(self.background.background_pos_x-7000, LIMITE_AGUA+80)
        self.botin5 = Botin(self.background.background_pos_x-1000, LIMITE_AGUA+100)
        self.hud = HUD(pantalla, self.buzo)# Crear una instancia de HUD
        self.clock = pygame.time.Clock()
        self.pantalla = pantalla

    def nivel_1(self, keys, tiempo_transcurrido):#lógica del bucle
        # Eventos de teclado
        self.buzo.control(keys)

        x_relativa = self.lvl_pos_x % self.background.ancho # Cálculo del movimiento del fondo basado en la posición del jugador
        if self.buzo.vivo:
            self.lvl_pos_x = self.background.scroll_background(self.buzo, self.tiburon1, self.tiburon2, self.tiburon3, self.lvl_pos_x)
            self.background.background_pos_x = x_relativa

        self.pantalla.fill((0, 0, 0))
        self.background.draw(self.pantalla, self.background.background_pos_x)

        if self.buzo.vivo:
            # Reemplaza la llamada anterior a self.botinX.esparcir_botin con el uso de los botines recién creados
            self.botin1.esparcir_botin(self.buzo, self.pantalla, self.background.background_pos_x-self.botin1.rect.width)
            self.botin2.esparcir_botin(self.buzo, self.pantalla, self.background.background_pos_x-self.botin2.rect.width)
            self.botin3.esparcir_botin(self.buzo, self.pantalla, self.background.background_pos_x-self.botin3.rect.width)
            self.botin4.esparcir_botin(self.buzo, self.pantalla, self.background.background_pos_x-self.botin4.rect.width)
            self.botin5.esparcir_botin(self.buzo, self.pantalla, self.background.background_pos_x-self.botin5.rect.width)
            self.buzo.update()
            self.buzo.draw(self.pantalla)
            self.tiburon1.update(tiempo_transcurrido)
            self.tiburon2.update(tiempo_transcurrido)
            self.tiburon3.update(tiempo_transcurrido)
            self.tiburon1.draw(self.pantalla, self.buzo)
            self.tiburon2.draw(self.pantalla, self.buzo)
            self.tiburon3.draw(self.pantalla, self.buzo)
            self.hud.actualizar_hud()
            if self.buzo.objetos >= 3:
                Pantallas.pantalla_fin_nivel(self.pantalla)
        else:
            Pantallas.pantalla_personaje_muerto(self.pantalla)