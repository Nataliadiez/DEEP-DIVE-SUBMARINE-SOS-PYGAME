import pygame
from constantes import *
import json

class Auxiliar:
    @staticmethod #se pone metodo estatico para no construir un objeto
    def getSurfaceFromSprite(path,cant_columnas,cant_filas,numero_fila, ancho, alto, color_key=False, color=None):#recorre todas las fotos
        lista = []
        surface_imagen = pygame.image.load(path)
        surface_imagen = pygame.transform.scale(surface_imagen, (ancho, alto))
        fotograma_ancho = int(surface_imagen.get_width()/cant_columnas)
        fotograma_alto = int(surface_imagen.get_height()/cant_filas)
        x = 0
        if color_key:
            surface_imagen.set_colorkey(color)
        for columna in range(cant_columnas):
            for fila in range (cant_filas):
                x = columna * fotograma_ancho
                y = numero_fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho, fotograma_alto)
                lista.append(surface_fotograma)
        return lista
    
    @staticmethod
    def colisiones(pantalla, color):
        #pygame.draw.rect(pantalla, color, buzo.rect, 1)
        #pygame.draw.rect(pantalla, COLOR_ROJO_PAINT, self.rect_colision, 1)
        pass

    @staticmethod
    def personalizar_img(ruta:str, scale=False, ancho=None, alto=None, color_key=False, color=None):
        imagen = pygame.image.load(ruta).convert()
        if scale:
            imagen = pygame.transform.scale(imagen, (ancho, alto))
        if color_key:
            imagen.set_colorkey(color)
        return imagen
    
    
    @staticmethod
    def animar_enemigos(lista)->None:
        for i in range (len(lista)):
            tiburon = lista
            if i <= 2:
                tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/Shark-Sheet.png", 8, 1, 0, ANCHO_TIBURON,ALTO_TIBURON, False, None)
            else:
                tiburon[i].set_animation(f"{PATH_IMAGE}/enemigos/pez_espada.png", 4, 1, 0, 300, 50, False, None)
    
    @staticmethod
    def ordenar_puntajes(lista_datos, score):
        return sorted(lista_datos, key=lambda x: x[score], reverse=True)


    #TODO usar esta lógica para guardar los puntajes en vez de la música

