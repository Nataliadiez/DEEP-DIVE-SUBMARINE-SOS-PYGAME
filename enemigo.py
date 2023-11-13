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
        self.alto_imagen = self.imagen.get_width()
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
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
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
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
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
        self.cuerpo_jefe = pygame.image.load("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/cuerpo.png").convert()
        self.cuerpo_jefe.set_colorkey(COLOR_BLANCO)
        self.cuerpo_jefe = pygame.transform.scale(self.cuerpo_jefe, (400,300))
        self.animacion_ojos = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/ojitos.png",6,1,0,550,75)
        self.animacion_trompa = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/trompa.png",6,1,0,550,75)
        self.animacion_tentaculos = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/tentaculo1.png",6,1,0,1000,75)
        self.animacion_tentaculos_2 = Auxiliar.getSurfaceFromSprite("DEEP DIVE - SUBMARINE SOS/img/enemigos/kraken/tentaculo2.png",6,1,0,1000,75)
        
        self.img_ten_1 = self.animacion_tentaculos_2[0]
        self.img_ten_2 = self.animacion_tentaculos_2[1]
        self.img_ten_3 = self.animacion_tentaculos_2[2]
        self.img_ten_4 = self.animacion_tentaculos_2[3]
        self.img_ten_5 = self.animacion_tentaculos_2[4]
        self.img_ten_6 = self.animacion_tentaculos_2[5]
        self.img_ten_1_rect = self.img_ten_1.get_rect()
        self.img_ten_1_rect.x = 430
        self.img_ten_1_rect.y = 260

        
        self.frame = 0
        self.imagen_ojos = self.animacion_ojos[self.frame]
        self.alto_imagen_ojos = self.imagen_ojos.get_width()
        self.rect_imagen_ojos = self.imagen_ojos.get_rect()
        self.rect_imagen_ojos.x = 638
        self.rect_imagen_ojos.y = 293
        self.imagen_trompa = self.animacion_trompa[self.frame]
        self.rect_imagen_trompa = self.imagen_trompa.get_rect()
        self.rect_imagen_trompa.x = 500
        self.rect_imagen_trompa.y = 350

        self.imagen_tentaculo = self.animacion_tentaculos[self.frame]
        self.rect_imagen_tentaculo = self.imagen_tentaculo.get_rect()
        self.rect_imagen_tentaculo.x = 320
        self.rect_imagen_tentaculo.y = 260
        self.rect_imagen_tentaculo2_y = self.rect_imagen_tentaculo.y + 50
        self.rect_imagen_tentaculo3_y = self.rect_imagen_tentaculo.y + 100

        self.tiempo_transcurrido = 0
        self.tiempo_cambio_frame = 200  # Tiempo (en milisegundos) para cambiar de frame
        self.cuerpo_jefe_rect = self.cuerpo_jefe.get_rect()
        self.cuerpo_jefe_rect.x = 566
        self.cuerpo_jefe_rect.y = 200
        self.rect_colision = self.cuerpo_jefe_rect
        self.tiempo_transcurrido = 0
        self.vida = 100
        self.colision_con_bala = True
        


    def update(self, delta_tiempo):
        # Incrementar el tiempo transcurrido
        self.tiempo_transcurrido += delta_tiempo
        # Cambiar de frame si ha pasado el tiempo necesario
        if self.tiempo_transcurrido >= self.tiempo_cambio_frame:
            self.frame = (self.frame + 1) % len(self.animacion_ojos)
            self.imagen_ojos = self.animacion_ojos[self.frame]
            self.imagen_trompa = self.animacion_trompa[self.frame]
            self.imagen_tentaculo = self.animacion_tentaculos[self.frame]
            self.tiempo_transcurrido = 0  # Reiniciar el contador

    def draw(self, pantalla):
        #pygame.draw.rect(pantalla, COLOR_ROJO, self.cuerpo_jefe_rect)
        self.colision_con_bala = True
        pantalla.blit(self.cuerpo_jefe, self.cuerpo_jefe_rect)
        pantalla.blit(self.img_ten_1, (self.img_ten_1_rect.x, self.img_ten_1_rect.y+50))
        pantalla.blit(self.img_ten_2, (self.img_ten_1_rect.x+100, self.img_ten_1_rect.y+50))
        pantalla.blit(self.img_ten_1, (self.img_ten_1_rect.x, self.img_ten_1_rect.y+100))
        pantalla.blit(self.img_ten_2, (self.img_ten_1_rect.x+100, self.img_ten_1_rect.y+100))
        pantalla.blit(self.img_ten_1, (self.img_ten_1_rect.x, self.img_ten_1_rect.y))
        pantalla.blit(self.img_ten_2, (self.img_ten_1_rect.x+100, self.img_ten_1_rect.y))


        pantalla.blit(self.imagen_tentaculo, self.rect_imagen_tentaculo)
        pantalla.blit(self.imagen_tentaculo, (self.rect_imagen_tentaculo.x, self.rect_imagen_tentaculo2_y))
        pantalla.blit(self.imagen_tentaculo, (self.rect_imagen_tentaculo.x, self.rect_imagen_tentaculo3_y))
        
        
        #pantalla.blit(self.imagen_trompa, self.rect_imagen_trompa)
        pantalla.blit(self.imagen_ojos, self.rect_imagen_ojos)
        
        """ self.rect_colision = (self.rect_imagen.x+5, self.rect_imagen.y+10, 30, 30)
        if self.rect_imagen.x > -100:
            pantalla.blit(self.imagen, self.rect_imagen)
            #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        else:
            # La imagen del tiburón ha salido de la pantalla, reiniciar su posición
            self.rect_imagen.x = ANCHO_VENTANA - self.imagen.get_height()
            self.rect_imagen.y = random.randrange(LIMITE_AGUA+10, self.eje_y, 130)
            self.colision_tiburon = True """