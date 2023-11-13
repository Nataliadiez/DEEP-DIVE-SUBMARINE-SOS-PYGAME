import pygame
from constantes import *
from background import *
from enemigo import *
from player import *
from hud import *
from pantallas import Pantallas

class Nivel_1:
    def __init__(self, pantalla) -> None:
        self.background = Background("DEEP DIVE - SUBMARINE SOS/img/background/ecco3.png", 8442, ALTO_VENTANA, True)#background
        self.lvl_pos_x = 0 #logica scroll
        self.buzo = Buzo(50, LIMITE_AGUA+100, 5)#personaje
        self.tiburon1 = Tiburon()#creación de tiburones
        self.tiburon2 = Tiburon()
        self.tiburon3 = Tiburon()
        self.pez_espada1 = Pez_espada()
        self.pez_espada2 = Pez_espada()
        self.pez_espada3 = Pez_espada()
        self.lista_tiburones = [self.tiburon1, self.tiburon2, self.tiburon3, self.pez_espada1, self.pez_espada2, self.pez_espada3]
        self.botin1 = Botin(self.background.background_pos_x-4000, LIMITE_AGUA+50)
        self.botin2 = Botin(self.background.background_pos_x-5000, LIMITE_AGUA+200)
        self.botin3 = Botin(self.background.background_pos_x-6000, LIMITE_AGUA+20)
        self.lista_botines = [self.botin1, self.botin2, self.botin3]
        self.hud = HUD(pantalla, self.buzo)# Crear una instancia de HUD
        self.clock = pygame.time.Clock()
        self.pantalla = pantalla
        self.estado_nivel = False


    def renderizar_nivel(self, keys, tiempo_transcurrido, timer_segundos, sonido):#lógica del bucle
        # Eventos de teclado
        
        self.buzo.control(keys)
        if timer_segundos == 0:
            self.buzo.vivo = False

        x_relativa = self.lvl_pos_x % self.background.ancho # Cálculo del movimiento del fondo basado en la posición del jugador
        if self.buzo.vivo:
            self.buzo.mordida_tiburon = sonido.mordida_tiburon
            self.lvl_pos_x = self.background.scroll_background(self.buzo, self.lista_tiburones, self.lvl_pos_x)
            self.background.background_pos_x = x_relativa

        self.pantalla.fill((0, 0, 0))
        self.background.draw(self.pantalla, self.background.background_pos_x)

        if self.buzo.objetos == 3:
            Pantallas.pantalla_fin_nivel(self.pantalla)
            sonido.musica_fondo_lvl1.stop()
            sonido.efecto_agua.stop()
            self.estado_nivel = True
        else:
            if self.buzo.vivo:
                sonido.volumen_lvl1 = 0.7
                sonido.musica_fondo_lvl1.set_volume(sonido.volumen_lvl1)
                sonido.volumen_efecto_agua = 0.1
                sonido.efecto_agua.set_volume(sonido.volumen_efecto_agua)
                self.botin1.esparcir_botin(self.pantalla, self.background.background_pos_x-self.botin1.rect.width)
                self.botin2.esparcir_botin(self.pantalla, self.background.background_pos_x-self.botin2.rect.width)
                self.botin3.esparcir_botin(self.pantalla, self.background.background_pos_x-self.botin3.rect.width)
                self.buzo.update()
                self.buzo.draw(self.pantalla)
                for tiburon in self.lista_tiburones:
                    tiburon.update(tiempo_transcurrido)
                    tiburon.draw(self.pantalla)
                self.buzo.manejar_colisiones(self.lista_tiburones, self.lista_botines)
                self.hud.actualizar_hud(timer_segundos)
            
            else:
                Pantallas.pantalla_personaje_muerto(self.pantalla)
                sonido.musica_fondo_lvl1.stop()
                sonido.efecto_agua.stop()
                """ sonido.efecto_muerte_buzo.play()
                sonido.efecto_muerte_buzo.set_volume(0.0)
                sonido.efecto_muerte_buzo.stop() """


class Nivel_2(Nivel_1):
    def __init__(self, pantalla) -> None:
        super().__init__(pantalla)
        self.background = Background("DEEP DIVE - SUBMARINE SOS/img/background/cave.png")#background
        self.submarino = Submarino(50, LIMITE_AGUA+200, 5)#personaje
        self.submarino.limite_y = 100
        self.leviatan1 = Leviatan()
        self.leviatan2 = Leviatan()
        self.leviatan3 = Leviatan()
        self.pez_linterna1 = Pez_linterna()
        self.pez_linterna2 = Pez_linterna()
        self.pez_linterna3 = Pez_linterna()
        self.arma1 = Armas(self.background.background_pos_x-2000, LIMITE_AGUA+50)
        self.arma2 = Armas(self.background.background_pos_x-1000, LIMITE_AGUA+200)
        self.arma3 = Armas(self.background.background_pos_x-500, LIMITE_AGUA+20)
        self.lista_botines = [self.arma1, self.arma2, self.arma3]
        self.lista_leviatanes = [self.leviatan1, self.leviatan2, self.leviatan3, self.pez_linterna1, self.pez_linterna2, self.pez_linterna3]
        self.hud = HUD(pantalla, self.submarino)# Crear una instancia de HUD

    def renderizar_nivel(self, keys, tiempo_transcurrido, timer_segundos, sonido):#lógica del bucle
        # Eventos de teclado
        self.submarino.control(keys)
        if timer_segundos == 0:
            self.submarino.vivo = False

        x_relativa = self.lvl_pos_x % self.background.ancho # Cálculo del movimiento del fondo basado en la posición del jugador
        if self.submarino.vivo:
            self.submarino.mordida_leviatan = sonido.mordida_tiburon
            self.lvl_pos_x = self.background.scroll_background(self.submarino, self.lista_leviatanes, self.lvl_pos_x)
            self.background.background_pos_x = x_relativa

        self.pantalla.fill((0, 0, 0))
        self.background.draw(self.pantalla, self.background.background_pos_x)

        if self.submarino.objetos == 3:
            Pantallas.pantalla_fin_nivel(self.pantalla)
            sonido.musica_fondo_lvl1.stop()
            sonido.efecto_agua.stop()
        else:
            if self.submarino.vivo:
                sonido.volumen_lvl1 = 0.0
                sonido.musica_fondo_lvl1.set_volume(sonido.volumen_lvl1)
                sonido.volumen_efecto_agua = 0.1
                sonido.efecto_agua.set_volume(sonido.volumen_efecto_agua)
                self.arma1.esparcir_botin(self.pantalla, self.background.background_pos_x-self.arma1.rect.width)
                self.arma2.esparcir_botin(self.pantalla, self.background.background_pos_x-self.arma2.rect.width)
                self.arma3.esparcir_botin(self.pantalla, self.background.background_pos_x-self.arma3.rect.width)
                self.submarino.update()
                self.submarino.draw(self.pantalla)
                for leviatan in self.lista_leviatanes:
                    leviatan.update(tiempo_transcurrido)
                    leviatan.draw(self.pantalla)
                self.submarino.manejar_colisiones(self.lista_leviatanes, self.lista_botines)
                self.hud.actualizar_hud(timer_segundos)
            
            else:
                Pantallas.pantalla_personaje_muerto(self.pantalla)
                sonido.musica_fondo_lvl1.stop()
                sonido.efecto_agua.stop()
                
                """ sonido.efecto_muerte_buzo.play()
                sonido.efecto_muerte_buzo.set_volume(0.0)
                sonido.efecto_muerte_buzo.stop() """

class Nivel_3(Nivel_1):
    def __init__(self, pantalla) -> None:
        super().__init__(pantalla)
        self.background = StaticBackground("DEEP DIVE - SUBMARINE SOS/img/background/Underwater_Night_9.jpg", ANCHO_VENTANA, ALTO_VENTANA, True)#background
        self.submarino = Submarino_armas(50, LIMITE_AGUA+200, 5)#personaje
        self.submarino.limite_y = 100
        self.kraken = Kraken()
        self.hud = HUD(pantalla, self.submarino)# Crear una instancia de HUD

    def renderizar_nivel(self, keys, tiempo_transcurrido, timer_segundos, sonido):#lógica del bucle
        # Eventos de teclado
        self.submarino.control(keys)
        if timer_segundos == 0:
            self.submarino.vivo = False

        self.pantalla.fill((0, 0, 0))
        self.background.draw(self.pantalla)  # Llama al método draw sin cambiar la posición del fondo

        #TODO lógica para finalizar el nivel
        if self.kraken.vida == 0:
            Pantallas.pantalla_fin_nivel(self.pantalla)
            sonido.musica_fondo_lvl1.stop()
            sonido.efecto_agua.stop()
        else:
            if self.submarino.vivo:
                #TODO poner acá el sonido del jefe
                #self.submarino.golpe_jefe = sonido.golpe_jefe
                sonido.volumen_lvl1 = 0.0
                sonido.musica_fondo_lvl1.set_volume(sonido.volumen_lvl1)
                sonido.volumen_efecto_agua = 0.1
                sonido.efecto_agua.set_volume(sonido.volumen_efecto_agua)
                self.kraken.update(tiempo_transcurrido)
                self.kraken.draw(self.pantalla)
                self.submarino.update()
                self.submarino.draw(self.pantalla)
                self.submarino.manejar_colisiones(self.kraken)
                #self.submarino.manejar_colisiones(self.jefe)
                self.hud.actualizar_hud(timer_segundos)
            else:
                Pantallas.pantalla_personaje_muerto(self.pantalla)
                sonido.musica_fondo_lvl1.stop()
                sonido.efecto_agua.stop()
                