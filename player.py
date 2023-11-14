import pygame
from constantes import *
from auxiliar import Auxiliar
from enemigo import *


class Buzo:
    def __init__(self, x, y, velocidad):
        self.nadar_der = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/spritesheet-buzo-agua.png", 4, 4, 2, 170, 170)
        self.nadar_izq = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/spritesheet-buzo-agua.png", 4, 4, 1, 170, 170)
        self.nadar_arriba = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/spritesheet-buzo-agua.png", 4, 4, 3, 170, 170)
        self.nadar_abajo = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/spritesheet-buzo-agua.png", 4, 4, 0, 170, 170)
        self.posicion_x = x
        self.posicion_y = y
        self.velocidad = velocidad
        self.frame = 0
        self.vidas = 3
        self.porcentaje_vida = 60
        self.objetos = 0
        self.score = 0
        self.animation = self.nadar_der
        self.image = self.animation[self.frame]
        self.ancho_imagen = self.image.get_width()
        self.alto_imagen = self.image.get_height()
        self.img_pos_x = self.ancho_imagen
        self.vivo = True
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicion_x, self.posicion_y)
        self.limite_y = LIMITE_AGUA
        #colisiones
        self.num_colisiones = 0
        self.mordida_tiburon = None

    def control(self, keys):
        self.posicion_x = 0
        self.posicion_y = 0

        if keys[pygame.K_RIGHT]:
            self.posicion_x = self.velocidad
            self.animation = self.nadar_der
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_LEFT]:
            self.posicion_x = -self.velocidad
            self.animation = self.nadar_izq
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_UP]:
            self.posicion_y = -self.velocidad
            self.animation = self.nadar_arriba
            self.frame = (self.frame + 1) % len(self.animation)
        elif keys[pygame.K_DOWN]:
            self.posicion_y = self.velocidad
            self.animation = self.nadar_abajo
            self.frame = (self.frame + 1) % len(self.animation)
    
    def manejar_colisiones(self, lista_tiburones, lista_botines):
        for tiburon in lista_tiburones:
            if self.rect.colliderect(tiburon.rect_colision) and tiburon.colision_tiburon:
                self.porcentaje_vida -= 10
                self.num_colisiones += 1
                tiburon.colision_tiburon = False
                self.mordida_tiburon.play()
                print(self.num_colisiones)
            if self.porcentaje_vida <= 0:
                self.vivo = False
        for botin in lista_botines:
            if botin.visible and self.rect.colliderect(botin.rect) and botin.colision_botin:
                botin.visible = False
                self.objetos += 1
                botin.colision_botin = False  # Desactivar la colisión solo para este botín

    def update(self):
        x = self.rect.x + self.posicion_x
        y = self.rect.y + self.posicion_y
        if 0 <= x < ANCHO_VENTANA - self.ancho_imagen:
            self.rect.x = x
        if self.limite_y <= y < ALTO_VENTANA - self.alto_imagen:
            self.rect.y = y


    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect.topleft)


class Submarino(Buzo):
    def __init__(self, x, y, velocidad):
        super().__init__(x, y, velocidad)
        self.nadar_der = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/submarinoRIGHT.png", 7, 1, 0, 400, 50, True, COLOR_BLANCO)
        self.nadar_izq = Auxiliar.getSurfaceFromSprite(PATH_IMAGE+"/personaje/submarinoLEFT.png", 7, 1, 0, 400, 50, True, COLOR_BLANCO)
        self.direccion = "derecha"
        # Número de fotogramas entre cambios de animación
        self.frames_entre_cambios = 3
        self.frames_desde_ultimo_cambio = 0
        self.porcentaje_vida = 60
        self.objetos = 0
        self.score = 0 #TODO logica del score, que luego se va a sumar y se va a subir a la database
        self.animation = self.nadar_der
        self.image = self.animation[self.frame]
        self.ancho_imagen = self.image.get_width()
        self.alto_imagen = self.image.get_height()
        self.img_pos_x = self.ancho_imagen
        self.vivo = True
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posicion_x, self.posicion_y)
        self.limite_y = 240
        #colisiones
        self.num_colisiones = 0
        self.mordida_leviatan = None
        

    def control(self, keys):
        self.posicion_x = 0
        self.posicion_y = 0
        # Actualizar el contador de fotogramas desde el último cambio
        self.frames_desde_ultimo_cambio += 1

        if keys[pygame.K_RIGHT]:
            self.direccion = "derecha"
            self.posicion_x = self.velocidad
            self.animation = self.nadar_der
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_LEFT]:
            self.direccion = "izquierda"
            self.posicion_x = -self.velocidad
            self.animation = self.nadar_izq
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_UP]:
            if self.direccion == "derecha":
                self.animation = self.nadar_der
            elif self.direccion == "izquierda":
                self.animation = self.nadar_izq
            self.posicion_y = -self.velocidad
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_DOWN]:
            if self.direccion == "derecha":
                self.animation = self.nadar_der
            elif self.direccion == "izquierda":
                self.animation = self.nadar_izq
            self.posicion_y = self.velocidad
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        
    
    def manejar_colisiones(self, lista_tiburones, lista_botines):
        for tiburon in lista_tiburones:
            if self.rect.colliderect(tiburon.rect_colision) and tiburon.colision_tiburon:
                self.porcentaje_vida -= 20
                self.num_colisiones += 1
                tiburon.colision_tiburon = False
                self.mordida_leviatan.play()
                print(self.num_colisiones)
            if self.porcentaje_vida <= 0:
                self.vivo = False
        for botin in lista_botines:
            if botin.visible and self.rect.colliderect(botin.rect) and botin.colision_botin:
                botin.visible = False
                self.objetos += 1
                botin.colision_botin = False  # Desactivar la colisión solo para este botín

    def update(self):
        x = self.rect.x + self.posicion_x
        y = self.rect.y + self.posicion_y
        if 0 <= x < ANCHO_VENTANA - self.ancho_imagen:
            self.rect.x = x
        if self.limite_y <= y < ALTO_VENTANA - self.alto_imagen:
            self.rect.y = y

    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect.topleft)

class Submarino_armas(Submarino):
    def __init__(self, x, y, velocidad):
        super().__init__(x, y, velocidad)
        #logica balas
        self.bala = None
        self.balazos_atinados = 0
        self.disparo_del_enemigo = False
    
    def control(self, keys):
        self.posicion_x = 0
        self.posicion_y = 0
        # Actualizar el contador de fotogramas desde el último cambio
        self.frames_desde_ultimo_cambio += 1

        if keys[pygame.K_RIGHT]:
            self.direccion = "derecha"
            self.posicion_x = self.velocidad
            self.animation = self.nadar_der
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_LEFT]:
            self.direccion = "izquierda"
            self.posicion_x = -self.velocidad
            self.animation = self.nadar_izq
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_UP]:
            if self.direccion == "derecha":
                self.animation = self.nadar_der
            elif self.direccion == "izquierda":
                self.animation = self.nadar_izq
            self.posicion_y = -self.velocidad
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        elif keys[pygame.K_DOWN]:
            if self.direccion == "derecha":
                self.animation = self.nadar_der
            elif self.direccion == "izquierda":
                self.animation = self.nadar_izq
            self.posicion_y = self.velocidad
            if self.frames_desde_ultimo_cambio >= self.frames_entre_cambios:
                self.frame = (self.frame + 1) % len(self.animation)
                self.frames_desde_ultimo_cambio = 0  # Reiniciar el contador
        if keys[pygame.K_SPACE]:
            if self.direccion == "derecha":
                self.disparar()

    def manejar_colisiones(self, kraken):
        if self.bala:
            if self.bala.rect.colliderect(kraken.rectangulo_cuerpo_colision) and kraken.colision_con_bala:
                self.balazos_atinados += 1
                kraken.colision_con_bala = False
                self.bala.colision_bala = True
                print(f"balazos atinados: {self.balazos_atinados}")
                kraken.vida -= 10
            if kraken.vida == 0:
                print("Kraken muerto")
        for disparo in kraken.lista_rects:
            if self.rect.colliderect(disparo) and kraken.colision_fuego:
                print("bala le pegó al submarino")
                self.porcentaje_vida -= 20
                self.num_colisiones += 1
                print(self.num_colisiones)
                kraken.colision_fuego = False
            if self.porcentaje_vida <= 0:
                self.vivo = False


    def update(self):
        x = self.rect.x + self.posicion_x
        y = self.rect.y + self.posicion_y
        if 0 <= x < ANCHO_VENTANA - self.ancho_imagen:
            self.rect.x = x
        if self.limite_y <= y < ALTO_VENTANA - self.alto_imagen:
            self.rect.y = y
    
    def draw(self, screen):
        self.image = self.animation[self.frame]
        #pygame.draw.rect(screen, COLOR_ROJO, self.rect)
        screen.blit(self.image, self.rect.topleft)
        if self.bala:
            self.bala.update()
            #pygame.draw.rect(screen, COLOR_ROJO, self.bala.rect)
            screen.blit(self.bala.img_disparos, self.bala.rect)
            
            if self.bala.rect.x > ANCHO_VENTANA or self.bala.colision_bala: #reinicio para que salga otra bala
                self.bala = False
    
    def disparar(self):
        # Si no hay una bala en vuelo, crea una nueva bala y agrégala al grupo
        if not self.bala:
            self.bala = Bala(self.rect.right, self.rect.centery)

class Bala(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #TODO llamar a la función para imagenes
        self.img_disparos = pygame.image.load("DEEP DIVE - SUBMARINE SOS\img\personaje\misil.png").convert()
        pygame.transform.scale(self.img_disparos,(30, 30))
        self.img_disparos.set_colorkey(COLOR_BLANCO)
        self.rect = self.img_disparos.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocidad = 15
        self.colision_bala = False

    def update(self):
        self.rect.x += self.velocidad