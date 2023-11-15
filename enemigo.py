import pygame
from constantes import *
import random
from auxiliar import Auxiliar


class Tiburon:
    def __init__(self):
        self.velocidad = random.randrange(3, 10, 1) #velocidad
        self.lista_tiburones = []
        self.animation = None
        self.frame = 0
        self.eje_y = ALTO_VENTANA-31
        self.tiempo_transcurrido = 0
        self.tiempo_cambio_frame = 200  # Tiempo (en milisegundos) para cambiar de frame
        self.colision_tiburon = True
        
    def set_animation(self, sprite_path, frames, rows, start_frame, width, height, has_colorkey=False, colorkey=None):
        self.animation = Auxiliar.getSurfaceFromSprite(sprite_path, frames, rows, start_frame, width, height, has_colorkey, colorkey)
        self.imagen = self.animation[self.frame]
        self.rect_imagen = self.imagen.get_rect()
        self.rect_imagen.x = random.randrange(600, 2000, 300) #donde aparecen eje x
        self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 30) #donde aparecen eje y
        self.rect_colision = (self.rect_imagen.x ,self.rect_imagen.y,100,80)
        
    def update(self, delta_tiempo):
        # Incrementar el tiempo transcurrido
        self.tiempo_transcurrido += delta_tiempo
        # Cambiar de frame si ha pasado el tiempo necesario
        if self.tiempo_transcurrido >= self.tiempo_cambio_frame:
            self.frame = (self.frame + 1) % len(self.animation)
            self.imagen = self.animation[self.frame]
            self.tiempo_transcurrido = 0  # Reiniciar el contador
            
        self.rect_colision = (self.rect_imagen.x, self.rect_imagen.y + 20, 50, 30)
        self.rect_imagen.x -= self.velocidad

    def draw(self, pantalla):
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 130)
            self.colision_tiburon = True


class Leviatan(Tiburon):
    def __init__(self):
        super().__init__()
        self.set_animation(f"{PATH_IMAGE}/enemigos/leviatan2.png", 4, 1, 0, 1000, ALTO_TIBURON, True, COLOR_BLANCO)

    def draw(self, pantalla):
        self.rect_colision = (self.rect_imagen.x, self.rect_imagen.y + 10, 100, 50)
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 130)
            self.colision_tiburon = True

class Pez_linterna(Tiburon):
    def __init__(self):
        super().__init__()
        self.set_animation(f"{PATH_IMAGE}/enemigos/pez_linterna.png", 6, 1, 0, 300, 50, False, None)
    def draw(self, pantalla):
        self.rect_colision = (self.rect_imagen.x+5, self.rect_imagen.y+10, 30, 30)
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 130)
            self.colision_tiburon = True

class Pez_espada(Tiburon):
    def __init__(self):
        super().__init__()
        self.set_animation(f"{PATH_IMAGE}/enemigos/pez_espada.png", 4, 1, 0, 300, 50, False, None)
    def draw(self, pantalla):
        self.rect_colision = (self.rect_imagen.x+5, self.rect_imagen.y+10, 30, 30)
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 130)
            self.colision_tiburon = True

class Kraken():
    def __init__(self):
        self.cuerpo_jefe = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/cuerpo.png", True, 600, 300, True, COLOR_BLANCO)
        self.animacion_ojos = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/ojitos.png",6,1,0,550,75)
        self.animacion_tentaculos = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/tentaculo1.png",6,1,0,1000,75)
        self.proyectil = Auxiliar.personalizar_img("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/fueguito.png", True, 50, 30,  True, COLOR_BLANCO)
        self.frame = 0

        self.disparo_fuego = None

        self.rect_imagen_proyectil1 = self.proyectil.get_rect()
        self.rect_imagen_proyectil1.x = 380
        self.rect_imagen_proyectil1.y = 282

        self.rect_imagen_proyectil2 = self.proyectil.get_rect()
        self.rect_imagen_proyectil2.x = 380
        self.rect_imagen_proyectil2.y = 327

        self.rect_imagen_proyectil3 = self.proyectil.get_rect()
        self.rect_imagen_proyectil3.x = 380
        self.rect_imagen_proyectil3.y = 367

        self.rect_imagen_proyectil4 = self.proyectil.get_rect()
        self.rect_imagen_proyectil4.x = 380
        self.rect_imagen_proyectil4.y = 407

        self.imagen_ojos = self.animacion_ojos[self.frame]
        self.rect_imagen_ojos = self.imagen_ojos.get_rect()
        self.rect_imagen_ojos.x = 750
        self.rect_imagen_ojos.y = 293

        self.imagen_tentaculo = self.animacion_tentaculos[self.frame]
        self.rect_imagen_tentaculo = self.imagen_tentaculo.get_rect()
        self.rect_imagen_tentaculo.x = 350
        self.rect_imagen_tentaculo.y = 260
        self.lista_valores_y = [0, 45, 85, 125]
        self.rectangulo_cuerpo_colision = pygame.Rect(770, 300, 50, 50)

        self.tiempo_transcurrido = 0
        self.tiempo_cambio_frame = 200  # Tiempo (en milisegundos) para cambiar de frame
        self.cuerpo_jefe_rect = self.cuerpo_jefe.get_rect()
        self.cuerpo_jefe_rect.x = 450
        self.cuerpo_jefe_rect.y = 200
        self.rect_colision = self.cuerpo_jefe_rect
        self.tiempo_transcurrido = 0
        self.vida = 100
        self.colision_con_bala = True
        self.colision_fuego = True
        self.lista_rects = []

    def update(self, delta_tiempo):
        # Incrementar el tiempo transcurrido
        self.tiempo_transcurrido += delta_tiempo
        # Cambiar de frame si ha pasado el tiempo necesario
        if self.tiempo_transcurrido >= self.tiempo_cambio_frame: #verifica que pase el tiempo antes de cambiar de frame
            self.frame = (self.frame + 1) % len(self.animacion_ojos)
            self.imagen_ojos = self.animacion_ojos[self.frame]
            self.imagen_tentaculo = self.animacion_tentaculos[self.frame]
            self.tiempo_transcurrido = 0  # Reiniciar el contador
        
        velocidad_proyectil = 200
        tiempo = delta_tiempo / 1000
        proyectil = velocidad_proyectil * tiempo
        self.rect_imagen_proyectil1.x -= proyectil
        self.rect_imagen_proyectil2.x -= proyectil
        self.rect_imagen_proyectil3.x -= proyectil
        self.rect_imagen_proyectil4.x -= proyectil
        # Validar si la bala está fuera de la pantalla
        if self.rect_imagen_proyectil1.x < 0:
            # Reiniciar la posición de la bala
            self.rect_imagen_proyectil1.x = 380
            self.rect_imagen_proyectil2.x = 380
            self.rect_imagen_proyectil3.x = 380
            self.rect_imagen_proyectil4.x = 380
            self.colision_fuego = True
            self.disparo_fuego.play()

    def draw(self, pantalla, delta_tiempo):
        self.colision_con_bala = True

        pantalla.blit(self.cuerpo_jefe, self.cuerpo_jefe_rect)
        for numero in self.lista_valores_y:
            pantalla.blit(self.imagen_tentaculo, (self.rect_imagen_tentaculo.x, self.rect_imagen_tentaculo.y + numero))
        self.lista_rects.append(self.rect_imagen_proyectil1)
        self.lista_rects.append(self.rect_imagen_proyectil2)
        self.lista_rects.append(self.rect_imagen_proyectil3)
        self.lista_rects.append(self.rect_imagen_proyectil4)
        """ pygame.draw.rect(pantalla, COLOR_ROJO, self.rect_imagen_proyectil1)
        pygame.draw.rect(pantalla, COLOR_ROJO, self.rect_imagen_proyectil2)
        pygame.draw.rect(pantalla, COLOR_ROJO, self.rect_imagen_proyectil3)
        pygame.draw.rect(pantalla, COLOR_ROJO, self.rect_imagen_proyectil4) """
            
        pantalla.blit(self.proyectil, self.rect_imagen_proyectil1)
        pantalla.blit(self.proyectil, self.rect_imagen_proyectil2)
        pantalla.blit(self.proyectil, self.rect_imagen_proyectil3)
        pantalla.blit(self.proyectil, self.rect_imagen_proyectil4)
        pantalla.blit(self.imagen_ojos, self.rect_imagen_ojos)
        #pygame.draw.rect(pantalla, COLOR_ROJO, self.rectangulo_cuerpo_colision)
        