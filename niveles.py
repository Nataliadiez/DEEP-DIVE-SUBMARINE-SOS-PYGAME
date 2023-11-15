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
        self.botin1 = Botin(self.background.background_pos_x-5000, LIMITE_AGUA+50)
        self.botin2 = Botin(self.background.background_pos_x-6000, LIMITE_AGUA+200)
        self.botin3 = Botin(self.background.background_pos_x-7000, LIMITE_AGUA+20)#TODO volverlo a 6000
        self.lista_botines = [self.botin1, self.botin2, self.botin3]
        self.hud = HUD(pantalla, self.buzo)# Crear una instancia de HUD
        self.pantalla = pantalla
        self.estado_nivel = False
        self.blitear_pantalla_muerte = True
        self.animar_enemigos = True
        self.pantalla_carga = Pantallas(self.pantalla)
    
    def activar_animacion_enemigos(self):
        if self.animar_enemigos:
            Auxiliar.animar_enemigos(self.lista_tiburones)
            self.animar_enemigos = False

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

        self.background.draw(self.pantalla, self.background.background_pos_x)

        if self.buzo.objetos == 1:
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
                self.activar_animacion_enemigos()
                for tiburon in self.lista_tiburones:
                    tiburon.update(tiempo_transcurrido)
                    tiburon.draw(self.pantalla)
                self.buzo.manejar_colisiones(self.lista_tiburones, self.lista_botines)
                self.hud.actualizar_hud(timer_segundos, None, "nivel_1")
            else:
                if self.blitear_pantalla_muerte:
                    self.pantalla_carga.personaje_muerto()
                    sonido.musica_fondo_lvl1.stop()
                    sonido.efecto_agua.stop()
                else:
                    sonido.musica_fondo_lvl1.stop()
                    sonido.efecto_agua.stop()


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
        self.hud = HUD(pantalla, self.submarino)
        self.estado_nivel = False

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

        if self.submarino.objetos == 1:
            sonido.musica_fondo_lvl2.stop()
            sonido.efecto_agua.stop()
            self.estado_nivel = True
        else:
            if self.submarino.vivo:
                sonido.volumen_lvl2 = 0.1
                sonido.musica_fondo_lvl2.set_volume(sonido.volumen_lvl2)
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
                self.hud.actualizar_hud(timer_segundos, None, "nivel_2")
            
            else:
                if self.blitear_pantalla_muerte:
                    self.pantalla_carga.personaje_muerto()
                    sonido.volumen_lvl2 = 0.0
                    sonido.musica_fondo_lvl2.set_volume(sonido.volumen_lvl2)
                    sonido.musica_fondo_lvl2.stop()
                    sonido.efecto_agua.stop()
                else:
                    sonido.volumen_lvl2 = 0.0
                    sonido.musica_fondo_lvl2.set_volume(sonido.volumen_lvl2)
                    sonido.musica_fondo_lvl2.stop()
                    sonido.efecto_agua.stop()


class Nivel_3(Nivel_1):
    def __init__(self, pantalla) -> None:
        super().__init__(pantalla)
        self.background = StaticBackground("DEEP DIVE - SUBMARINE SOS/img/background/Underwater_Night_9.jpg", ANCHO_VENTANA, ALTO_VENTANA, True)#background
        self.submarino = Submarino_armas(50, LIMITE_AGUA+50, 5)#personaje
        self.submarino.limite_y = 100
        self.kraken = Kraken()
        self.hud = HUD(pantalla, self.submarino)# Crear una instancia de HUD
        self.kraken_muerto = True

    def renderizar_nivel(self, keys, tiempo_transcurrido, timer_segundos, sonido):#lógica del bucle
        # Eventos de teclado
        self.submarino.control(keys)
        if timer_segundos == 0:
            self.submarino.vivo = False

        self.pantalla.fill((0, 0, 0))
        self.background.draw(self.pantalla)  # Llama al método draw sin cambiar la posición del fondo

        #TODO lógica para finalizar el nivel
        if self.kraken.vida == 0:
            #TODO pantalla para el fin del juego
            sonido.musica_fondo_lvl3.stop()
            sonido.efecto_agua.stop()
            if self.kraken_muerto:
                sonido.muerte_kraken.play()
                self.kraken_muerto = False
            self.pantalla_carga.pantalla_fin_juego()
        else:
            if self.submarino.vivo:
                self.submarino.hits_kraken = sonido.hits_kraken
                self.submarino.misil = sonido.misil
                self.kraken.disparo_fuego = sonido.fuego
                #TODO poner acá el sonido del jefe
                #self.submarino.golpe_jefe = sonido.golpe_jefe
                sonido.volumen_lvl3 = 0.2
                sonido.musica_fondo_lvl3.set_volume(sonido.volumen_lvl3)
                sonido.volumen_efecto_agua = 0.1
                sonido.efecto_agua.set_volume(sonido.volumen_efecto_agua)
                self.kraken.update(tiempo_transcurrido)
                self.kraken.draw(self.pantalla, tiempo_transcurrido)
                self.submarino.update()
                self.submarino.draw(self.pantalla)
                self.submarino.manejar_colisiones(self.kraken)
                self.hud.actualizar_hud(timer_segundos,self.kraken, "nivel_3")
            else:
                if self.blitear_pantalla_muerte:
                    self.pantalla_carga.personaje_muerto()
                else:
                    sonido.volumen_lvl3 = 0.0
                    sonido.musica_fondo_lvl3.set_volume(sonido.volumen_lvl3)
                    sonido.musica_fondo_lvl3.stop()
                    sonido.efecto_agua.stop()
                